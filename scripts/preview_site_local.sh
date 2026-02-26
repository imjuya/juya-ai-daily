#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TOOLS_DIR="${ROOT_DIR}/.local-tools"
OUTPUT_DIR="${ROOT_DIR}/output"
PREVIEW_ROOT="${OUTPUT_DIR}/preview-root"
SITE_SUBPATH="juya-ai-daily"

ISITE_VERSION="${ISITE_VERSION:-v0.2.4}"
ZOLA_VERSION="${ZOLA_VERSION:-v0.20.0}"
PORT="${PORT:-4173}"
SERVE="${SERVE:-1}"
FORCE_REDOWNLOAD="${FORCE_REDOWNLOAD:-0}"
BUILD_MODE="${BUILD_MODE:-generate}"

REPO_OWNER="${REPO_OWNER:-imjuya}"
REPO_NAME="${REPO_NAME:-juya-ai-daily}"
BASE_URL="${BASE_URL:-http://127.0.0.1:${PORT}/${SITE_SUBPATH}}"
LIVE_URL="${LIVE_URL:-https://${REPO_OWNER}.github.io/${REPO_NAME}}"

usage() {
  cat <<'EOF'
Usage: scripts/preview_site_local.sh [options]

Options:
  --owner <owner>       GitHub owner for isite generate (default: imjuya)
  --repo <repo>         GitHub repo for isite generate (default: juya-ai-daily)
  --base-url <url>      Zola base URL (default: http://127.0.0.1:4173/juya-ai-daily)
  --live-url <url>      Live site URL for snapshot mode (default: https://imjuya.github.io/juya-ai-daily)
  --skip-generate       Reuse existing output/public only (no GitHub API)
  --snapshot-live       Download live GitHub Pages snapshot (no GitHub API token)
  --port <port>         Local preview port (default: 4173)
  --no-serve            Build only, do not start local server
  --force-redownload    Redownload isite/zola binaries
  -h, --help            Show help
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --owner)
      REPO_OWNER="$2"
      shift 2
      ;;
    --repo)
      REPO_NAME="$2"
      shift 2
      ;;
    --base-url)
      BASE_URL="$2"
      shift 2
      ;;
    --live-url)
      LIVE_URL="$2"
      shift 2
      ;;
    --skip-generate)
      BUILD_MODE="skip"
      shift
      ;;
    --snapshot-live)
      BUILD_MODE="snapshot"
      shift
      ;;
    --port)
      PORT="$2"
      shift 2
      ;;
    --no-serve)
      SERVE=0
      shift
      ;;
    --force-redownload)
      FORCE_REDOWNLOAD=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage
      exit 1
      ;;
  esac
done

os="$(uname -s | tr '[:upper:]' '[:lower:]')"
arch="$(uname -m)"

isite_platform=""
zola_platform=""

case "${os}-${arch}" in
  linux-x86_64)
    isite_platform="linux_amd64"
    zola_platform="x86_64-unknown-linux-gnu"
    ;;
  linux-aarch64|linux-arm64)
    isite_platform="linux_arm64"
    zola_platform="aarch64-unknown-linux-gnu"
    ;;
  darwin-x86_64)
    isite_platform="darwin_amd64"
    zola_platform="x86_64-apple-darwin"
    ;;
  darwin-arm64)
    isite_platform="darwin_arm64"
    zola_platform="aarch64-apple-darwin"
    ;;
  *)
    echo "Unsupported platform: ${os}-${arch}" >&2
    exit 1
    ;;
esac

mkdir -p "${TOOLS_DIR}"

download_and_extract_tar() {
  local url="$1"
  local bin_name="$2"
  local target_bin="$3"
  local temp_dir
  temp_dir="$(mktemp -d)"
  local archive="${temp_dir}/archive.tar.gz"

  echo "Downloading ${url}" >&2
  curl -fsSL "${url}" -o "${archive}"
  tar -xzf "${archive}" -C "${temp_dir}"

  local found_bin
  found_bin="$(find "${temp_dir}" -type f -name "${bin_name}" | head -n 1 || true)"
  if [[ -z "${found_bin}" ]]; then
    echo "Could not find binary '${bin_name}' in downloaded archive: ${url}" >&2
    exit 1
  fi

  mkdir -p "$(dirname "${target_bin}")"
  cp "${found_bin}" "${target_bin}"
  chmod +x "${target_bin}"
}

ensure_isite() {
  local version_no_v="${ISITE_VERSION#v}"
  local bin_path="${TOOLS_DIR}/isite/${ISITE_VERSION}/isite"
  local url="https://github.com/kemingy/isite/releases/download/${ISITE_VERSION}/isite_${version_no_v}_${isite_platform}.tar.gz"

  if [[ "${FORCE_REDOWNLOAD}" == "1" ]]; then
    rm -f "${bin_path}"
  fi
  if [[ ! -x "${bin_path}" ]]; then
    download_and_extract_tar "${url}" "isite" "${bin_path}"
  fi
  echo "${bin_path}"
}

ensure_zola() {
  local bin_path="${TOOLS_DIR}/zola/${ZOLA_VERSION}/zola"
  local url="https://github.com/getzola/zola/releases/download/${ZOLA_VERSION}/zola-${ZOLA_VERSION}-${zola_platform}.tar.gz"

  if [[ "${FORCE_REDOWNLOAD}" == "1" ]]; then
    rm -f "${bin_path}"
  fi
  if [[ ! -x "${bin_path}" ]]; then
    download_and_extract_tar "${url}" "zola" "${bin_path}"
  fi
  echo "${bin_path}"
}

sed_inplace() {
  local expr="$1"
  local file="$2"
  if sed --version >/dev/null 2>&1; then
    sed -i "${expr}" "${file}"
  else
    sed -i '' "${expr}" "${file}"
  fi
}

snapshot_from_live() {
  local live_url="$1"
  local snapshot_dir="${OUTPUT_DIR}/live-snapshot"
  local url_no_proto host path mirror_src

  rm -rf "${OUTPUT_DIR}"
  mkdir -p "${OUTPUT_DIR}"
  mkdir -p "${snapshot_dir}"

  set +e
  wget \
    --mirror \
    --no-verbose \
    --no-parent \
    --convert-links \
    --adjust-extension \
    --page-requisites \
    --directory-prefix "${snapshot_dir}" \
    "${live_url}/"
  local wget_rc=$?
  set -e
  if [[ "${wget_rc}" -ne 0 && "${wget_rc}" -ne 8 ]]; then
    echo "wget failed with exit code ${wget_rc}" >&2
    exit "${wget_rc}"
  fi

  url_no_proto="${live_url#https://}"
  url_no_proto="${url_no_proto#http://}"
  host="${url_no_proto%%/*}"
  if [[ "${url_no_proto}" == "${host}" ]]; then
    path="/"
  else
    path="/${url_no_proto#*/}"
  fi
  path="${path%/}"
  if [[ -z "${path}" ]]; then
    mirror_src="${snapshot_dir}/${host}"
  else
    mirror_src="${snapshot_dir}/${host}${path}"
  fi

  if [[ ! -d "${mirror_src}" ]]; then
    echo "Live snapshot directory not found: ${mirror_src}" >&2
    exit 1
  fi

  mkdir -p "${OUTPUT_DIR}/public"
  cp -r "${mirror_src}/." "${OUTPUT_DIR}/public/"
}

echo "Build mode:  ${BUILD_MODE}"
echo "Base URL:    ${BASE_URL}"
echo "Live URL:    ${LIVE_URL}"

cd "${ROOT_DIR}"

case "${BUILD_MODE}" in
  generate)
    ISITE_BIN="$(ensure_isite)"
    ZOLA_BIN="$(ensure_zola)"
    echo "Using isite: ${ISITE_BIN}"
    echo "Using zola:  ${ZOLA_BIN}"

    rm -rf "${OUTPUT_DIR}"
    "${ISITE_BIN}" generate --user "${REPO_OWNER}" --repo "${REPO_NAME}"
    cp config.toml "${OUTPUT_DIR}/config.toml"

    mkdir -p "${OUTPUT_DIR}/static"
    cp -r static/. "${OUTPUT_DIR}/static/"
    test -f "${OUTPUT_DIR}/static/custom.css"

    (
      cd "${OUTPUT_DIR}"
      "${ZOLA_BIN}" build --base-url "${BASE_URL}"
    )
    ;;
  skip)
    if [[ ! -d "${OUTPUT_DIR}/public" ]]; then
      echo "output/public not found. Run with --snapshot-live or without --skip-generate first." >&2
      exit 1
    fi
    ;;
  snapshot)
    snapshot_from_live "${LIVE_URL}"
    ;;
  *)
    echo "Unsupported build mode: ${BUILD_MODE}" >&2
    exit 1
    ;;
esac

mkdir -p "${OUTPUT_DIR}/public"
cp static/custom.css "${OUTPUT_DIR}/public/custom.css"
test -f "${OUTPUT_DIR}/public/custom.css"

CSS_HREF="${BASE_URL%/}/custom.css"
# 改进的 JS 热重载代码：后台拉取 CSS 内容，对比有没有变化，只有发生变化时才更新 href，防止屏幕一直闪烁
LIVERELOAD_SCRIPT='<script id="css-live-reload">let lastCss="";setInterval(async()=>{try{const link=Array.from(document.querySelectorAll("link[rel=stylesheet]")).find(l=>l.href.includes("custom.css"));if(!link)return;const res=await fetch(link.href.split("?")[0]+"?t="+Date.now());const text=await res.text();if(lastCss&&lastCss!==text){link.href=link.href.split("?")[0]+"?t="+Date.now();}lastCss=text;}catch(e){}},1000);</script>'

while IFS= read -r html_file; do
  if ! rg -q 'href="[^"]*custom\.css"' "${html_file}"; then
    sed_inplace "s|</head>|<link rel=\"stylesheet\" href=\"${CSS_HREF}\"></head>|g" "${html_file}"
  fi
  
  if ! rg -q 'id="css-live-reload"' "${html_file}"; then
    sed_inplace "s|</body>|${LIVERELOAD_SCRIPT}</body>|g" "${html_file}"
  fi
done < <(find "${OUTPUT_DIR}/public" -name "*.html")

mkdir -p "${PREVIEW_ROOT}/${SITE_SUBPATH}"
rm -rf "${PREVIEW_ROOT:?}/${SITE_SUBPATH:?}"/*
cp -r "${OUTPUT_DIR}/public/." "${PREVIEW_ROOT}/${SITE_SUBPATH}/"

# 将 custom.css 替换为软链接，指向代码库中的源文件
# 这样你只修改 static/custom.css 就可以在浏览器里刷新看到生效，无须杀掉重启这个脚本
ln -sf "${ROOT_DIR}/static/custom.css" "${PREVIEW_ROOT}/${SITE_SUBPATH}/custom.css"

echo "Build complete:"
echo "  ${OUTPUT_DIR}/public"
echo "Preview root:"
echo "  ${PREVIEW_ROOT}/${SITE_SUBPATH}"
echo "Check CSS:"
echo "  ${PREVIEW_ROOT}/${SITE_SUBPATH}/custom.css"

if [[ "${SERVE}" == "1" ]]; then
  echo
  echo "Serving local preview at:"
  echo "  http://127.0.0.1:${PORT}/${SITE_SUBPATH}/"
  exec python3 -m http.server "${PORT}" --directory "${PREVIEW_ROOT}"
fi
