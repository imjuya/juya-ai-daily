# -*- coding: utf-8 -*-
import argparse
import html
import os
import re

import markdown
from feedgen.ext.base import BaseExtension
from feedgen.feed import FeedGenerator
from github import Github
from lxml import html as lxml_html
from lxml import etree as lxml_etree
from lxml.etree import tostring
from marko.ext.gfm import gfm as marko

PRIMARY_FEED_FILENAME = "rss.xml"
FEED_ICON_PATH = "static/icon.png"
FEED_ICON_SIZE = 144
RSS_SUMMARY_MAX_CHARS = 360
WEBFEEDS_NS = "http://webfeeds.org/rss/1.0"

MD_HEAD = """# 橘鸦AI早报

> 本仓库将AI早报备份为Markdown存档并自动生成RSS订阅。资讯内容由AI辅助生成，可能存在错误，请以原始信息出处和官方信息为准。内容从互联网上获取，如有侵权请联系删除。

正式订阅地址：https://imjuya.github.io/juya-ai-daily/rss.xml

## Links

| Platform | Link |
| :--- | :--- |
| RSS Feed | [Subscribe]({feed_subscribe_url}) |
| Markdown 备份 | [BACKUP](https://github.com/{repo_name}/tree/{branch_name}/BACKUP) |
| GitHub Pages | [View](https://imjuya.github.io/juya-ai-daily/) |
| 第三方多功能阅读器（@ViggoZ 制作） | [juya-daily](https://viggoz.github.io/juya-daily/) |
| AI早报 视频版-Bilibili | [Bilibili](https://space.bilibili.com/285286947) |
| AI早报 视频版-YouTube | [YouTube](https://www.youtube.com/@imjuya) |

---

"""

BACKUP_DIR = "BACKUP"
ANCHOR_NUMBER = 5
TOP_ISSUES_LABELS = ["Top"]
TODO_ISSUES_LABELS = ["TODO"]
FRIENDS_LABELS = ["Friends"]
ABOUT_LABELS = ["About"]
THINGS_LABELS = ["Things"]
IGNORE_LABELS = (
    FRIENDS_LABELS
    + TOP_ISSUES_LABELS
    + TODO_ISSUES_LABELS
    + ABOUT_LABELS
    + THINGS_LABELS
)

FRIENDS_TABLE_HEAD = "| Name | Link | Desc | \n | ---- | ---- | ---- |\n"
FRIENDS_TABLE_TEMPLATE = "| {name} | {link} | {desc} |\n"
FRIENDS_INFO_DICT = {
    "名字": "",
    "链接": "",
    "描述": "",
}


def get_me(user):
    return user.get_user().login


def get_me_from_repo(repo):
    return repo.owner.login


def is_me(issue, me):
    return issue.user.login == me


def is_hearted_by_me(comment, me):
    reactions = list(comment.get_reactions())
    for r in reactions:
        if r.content == "heart" and r.user.login == me:
            return True
    return False


def _make_friend_table_string(s):
    info_dict = FRIENDS_INFO_DICT.copy()
    try:
        string_list = s.splitlines()
        # drop empty line
        string_list = [l for l in string_list if l and not l.isspace()]
        for l in string_list:
            string_info_list = re.split("：", l)
            if len(string_info_list) < 2:
                continue
            info_dict[string_info_list[0]] = string_info_list[1]
        return FRIENDS_TABLE_TEMPLATE.format(
            name=info_dict["名字"], link=info_dict["链接"], desc=info_dict["描述"]
        )
    except Exception as e:
        print(str(e))
        return


# help to covert xml vaild string
def _valid_xml_char_ordinal(c):
    codepoint = ord(c)
    # conditions ordered by presumed frequency
    return (
        0x20 <= codepoint <= 0xD7FF
        or codepoint in (0x9, 0xA, 0xD)
        or 0xE000 <= codepoint <= 0xFFFD
        or 0x10000 <= codepoint <= 0x10FFFF
    )


def format_time(time):
    return str(time)[:10]


def get_pages_base_url(repo_name):
    owner, repo = repo_name.split("/", 1)
    return f"https://{owner}.github.io/{repo}"


def get_pages_feed_url(repo_name, feed_filename):
    return f"{get_pages_base_url(repo_name)}/{feed_filename}"


def get_repo_pages_feed_url(repo, feed_filename):
    return f"https://{repo.owner.login}.github.io/{repo.name}/{feed_filename}"


def get_repo_pages_issue_url(repo, issue_number):
    return f"https://{repo.owner.login}.github.io/{repo.name}/issue-{issue_number}/"


def login(token):
    return Github(token)


def get_repo(user: Github, repo: str):
    return user.get_repo(repo)


def parse_TODO(issue):
    body = (issue.body or "").splitlines()
    todo_undone = [l for l in body if l.startswith("- [ ] ")]
    todo_done = [l for l in body if l.startswith("- [x] ")]
    # just add info all done
    if not todo_undone:
        return f"[{issue.title}]({issue.html_url}) all done", []
    return (
        f"[{issue.title}]({issue.html_url})--{len(todo_undone)} jobs to do--{len(todo_done)} jobs done",
        todo_done + todo_undone,
    )


def get_top_issues(repo):
    return repo.get_issues(labels=TOP_ISSUES_LABELS, state="all")


def get_todo_issues(repo):
    return repo.get_issues(labels=TODO_ISSUES_LABELS, state="open")


def get_repo_labels(repo):
    return [l for l in repo.get_labels()]


def get_issues_from_label(repo, label):
    return repo.get_issues(labels=(label,), state="all")


def add_issue_info(issue, md):
    time = format_time(issue.created_at)
    md.write(f"- [{issue.title}]({issue.html_url})--{time}\n")


def add_md_todo(repo, md, me):
    todo_issues = list(get_todo_issues(repo))
    if not TODO_ISSUES_LABELS or not todo_issues:
        return
    with open(md, "a+", encoding="utf-8") as md:
        md.write("## TODO\n")
        for issue in todo_issues:
            if is_me(issue, me):
                todo_title, todo_list = parse_TODO(issue)
                md.write("TODO list from " + todo_title + "\n")
                for t in todo_list:
                    md.write(t + "\n")
                # new line
                md.write("\n")


def add_md_top(repo, md, me):
    top_issues = list(get_top_issues(repo))
    if not TOP_ISSUES_LABELS or not top_issues:
        return
    with open(md, "a+", encoding="utf-8") as md:
        md.write("## 置顶文章\n")
        for issue in top_issues:
            if is_me(issue, me):
                add_issue_info(issue, md)


def add_md_firends(repo, md, me):

    s = FRIENDS_TABLE_HEAD
    friends_issues = list(repo.get_issues(labels=FRIENDS_LABELS, state="all"))
    if not FRIENDS_LABELS or not friends_issues:
        return
    friends_issue_number = friends_issues[0].number
    for issue in friends_issues:
        for comment in issue.get_comments():
            if is_hearted_by_me(comment, me):
                try:
                    s += _make_friend_table_string(comment.body or "")
                except Exception as e:
                    print(str(e))
                    pass
    s = markdown.markdown(s, output_format="html", extensions=["extra"])
    with open(md, "a+", encoding="utf-8") as md:
        md.write(
            f"## [友情链接](https://github.com/{repo.full_name}/issues/{friends_issue_number})\n"
        )
        md.write("<details><summary>显示</summary>\n")
        md.write(s)
        md.write("</details>\n")
        md.write("\n\n")


def add_md_recent(repo, md, me, limit=5):
    count = 0
    with open(md, "a+", encoding="utf-8") as md:
        # one the issue that only one issue and delete (pyGitHub raise an exception)
        try:
            md.write("## 最近更新\n")
            for issue in repo.get_issues(state="all", sort="created", direction="desc"):
                if issue.pull_request:
                    continue
                if is_me(issue, me):
                    add_issue_info(issue, md)
                    count += 1
                    if count >= limit:
                        break
        except Exception as e:
            print(str(e))


def add_md_header(md, repo_name, feed_filename, branch_name):
    with open(md, "w", encoding="utf-8") as md:
        md.write(
            MD_HEAD.format(
                repo_name=repo_name,
                branch_name=branch_name,
                feed_subscribe_url=get_pages_feed_url(repo_name, feed_filename),
            )
        )
        md.write("\n")


def add_md_label(repo, md, me):
    labels = get_repo_labels(repo)

    # sort lables by description info if it exists, otherwise sort by name,
    # for example, we can let the description start with a number (1#Java, 2#Docker, 3#K8s, etc.)
    labels = sorted(
        labels,
        key=lambda x: (
            x.description is None,
            x.description == "",
            x.description,
            x.name,
        ),
    )

    with open(md, "a+", encoding="utf-8") as md:
        for label in labels:
            # we don't need add top label again
            if label.name in IGNORE_LABELS:
                continue

            issues = get_issues_from_label(repo, label)
            issues = list(sorted(issues, key=lambda x: x.created_at, reverse=True))
            if len(issues) != 0:
                md.write("## " + label.name + "\n\n")
            i = 0
            for issue in issues:
                if not issue:
                    continue
                if is_me(issue, me):
                    if i == ANCHOR_NUMBER:
                        md.write("<details><summary>显示更多</summary>\n")
                        md.write("\n")
                    add_issue_info(issue, md)
                    i += 1
            if i > ANCHOR_NUMBER:
                md.write("</details>\n")
                md.write("\n")


def add_md_footer(md):
    """Add footer with credits to the original author"""
    footer = """
---

## License

- 代码（脚本与站点生成逻辑，基于 [yihong0618/gitblog](https://github.com/yihong0618/gitblog)）：[MIT](./LICENSE)
- 文章内容（`BACKUP/`、`rss.xml`）：[CC BY-NC 4.0](./LICENSE-CONTENT)
- 转载要求：署名，禁止商用
- 第三方素材除外，按原权利声明

---

## Credits

Built with [gitblog](https://github.com/yihong0618/gitblog) by [@yihong0618](https://github.com/yihong0618)
"""
    with open(md, "a+", encoding="utf-8") as md_file:
        md_file.write(footer)


def get_to_generate_issues(repo, dir_name, me, issue_number=None):
    md_files = os.listdir(dir_name)
    generated_issues_numbers = [
        int(i.split("_")[0]) for i in md_files if i.split("_")[0].isdigit()
    ]
    to_generate_issues = [
        i
        for i in list(repo.get_issues(state="all", sort="created", direction="desc"))
        if int(i.number) not in generated_issues_numbers
        and i.body
        and is_me(i, me)
        and not i.pull_request
    ]
    if issue_number:
        issue = repo.get_issue(int(issue_number))
        issue_numbers = {i.number for i in to_generate_issues}
        if issue.number not in issue_numbers and issue.body and is_me(issue, me) and not issue.pull_request:
            to_generate_issues.append(issue)
    return to_generate_issues


def normalize_rss_html(content):
    try:
        fragments = lxml_html.fragments_fromstring(content)
        normalized = []
        for fragment in fragments:
            if isinstance(fragment, str):
                normalized.append(fragment)
            else:
                normalized.append(tostring(fragment, encoding="unicode", method="html"))
        return "".join(normalized)
    except Exception:
        return content


def html_to_plain_text(content):
    try:
        fragment = lxml_html.fragment_fromstring(content, create_parent="div")
        text = fragment.text_content()
    except Exception:
        text = re.sub(r"<[^>]+>", " ", content)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def make_rss_summary(content, max_chars=RSS_SUMMARY_MAX_CHARS):
    summary = html_to_plain_text(content)
    if len(summary) <= max_chars:
        return summary
    return summary[: max_chars - 1].rstrip() + "…"


class WebfeedsExtension(BaseExtension):
    def __init__(self):
        self._icon = None
        self._logo = None

    def extend_ns(self):
        return {"webfeeds": WEBFEEDS_NS}

    def extend_rss(self, rss_feed):
        channel = rss_feed[0]
        if self._icon:
            icon = lxml_etree.SubElement(channel, f"{{{WEBFEEDS_NS}}}icon")
            icon.text = self._icon
        if self._logo:
            logo = lxml_etree.SubElement(channel, f"{{{WEBFEEDS_NS}}}logo")
            logo.text = self._logo
        return rss_feed

    def icon(self, value=None):
        if value is not None:
            self._icon = value
        return self._icon

    def logo(self, value=None):
        if value is not None:
            self._logo = value
        return self._logo


def generate_rss_feed(repo, filename, me):
    pages_site_url = f"{get_pages_base_url(repo.full_name)}/"
    feed_self_url = get_repo_pages_feed_url(repo, filename)
    generator = FeedGenerator()
    generator.id(repo.html_url)
    generator.title("橘鸦AI早报")
    generator.description("资讯内容由AI辅助生成，可能存在错误，请以原始信息出处和官方信息为准。")
    generator.language("zh-CN")
    generator.author(
        {"name": "Juya", "email": "imjuyaya@gmail.com"}
    )
    generator.link(
        href=feed_self_url,
        rel="self",
        type="application/rss+xml",
    )
    generator.link(href=pages_site_url)
    feed_icon_url = f"{pages_site_url}icon.png"
    if os.path.exists(FEED_ICON_PATH):
        generator.load_extension("podcast")
        generator.podcast.itunes_image(feed_icon_url)
        generator.register_extension(
            "webfeeds",
            extension_class_feed=WebfeedsExtension,
            atom=False,
            rss=True,
        )
        generator.webfeeds.icon(feed_icon_url)
        generator.webfeeds.logo(feed_icon_url)
        generator.image(
            url=feed_icon_url,
            title="橘鸦AI早报",
            link=pages_site_url,
            width=str(FEED_ICON_SIZE),
            height=str(FEED_ICON_SIZE),
            description="橘鸦AI早报 RSS 图标",
        )
    for issue in repo.get_issues(state="all", sort="created", direction="desc"):
        if not issue.body or not is_me(issue, me) or issue.pull_request:
            continue
        issue_pages_url = get_repo_pages_issue_url(repo, issue.number)
        item = generator.add_entry(order="append")
        item.id(issue.html_url)
        item.link(href=issue_pages_url)
        item.title(issue.title)
        item.author({"name": "Juya"})
        item.published(issue.created_at.strftime("%Y-%m-%dT%H:%M:%SZ"))
        for label in issue.labels:
            item.category({"term": label.name})
        body = "".join(c for c in issue.body if _valid_xml_char_ordinal(c))
        full_content = normalize_rss_html(marko.convert(body))
        summary = make_rss_summary(full_content) or issue.title
        item.description(summary)
        item.content(full_content, type="CDATA")
    generator.rss_file(filename)


def main(token, repo_name, issue_number=None, dir_name=BACKUP_DIR):
    user = login(token)
    repo = get_repo(user, repo_name)
    me = get_me_from_repo(repo)
    default_branch = repo.default_branch or "master"
    # add to readme one by one, change order here
    add_md_header("README.md", repo_name, PRIMARY_FEED_FILENAME, default_branch)
    for func in [add_md_firends, add_md_top, add_md_recent, add_md_label, add_md_todo]:
        func(repo, "README.md", me)

    # add footer with credits
    add_md_footer("README.md")

    generate_rss_feed(repo, PRIMARY_FEED_FILENAME, me)
    to_generate_issues = get_to_generate_issues(repo, dir_name, me, issue_number)

    # save md files to backup folder
    for issue in to_generate_issues:
        save_issue(issue, me, dir_name)


def save_issue(issue, me, dir_name=BACKUP_DIR):
    md_name = os.path.join(
        dir_name, f"{issue.number}_{issue.title.replace('/', '-').replace(' ', '.')}.md"
    )
    with open(md_name, "w", encoding="utf-8") as f:
        f.write(f"# [{issue.title}]({issue.html_url})\n\n")
        f.write(issue.body or "")
        if issue.comments:
            for c in issue.get_comments():
                if is_me(c, me):
                    f.write("\n\n---\n\n")
                    f.write(c.body or "")


if __name__ == "__main__":
    if not os.path.exists(BACKUP_DIR):
        os.mkdir(BACKUP_DIR)
    parser = argparse.ArgumentParser()
    parser.add_argument("github_token", help="github_token")
    parser.add_argument("repo_name", help="repo_name")
    parser.add_argument(
        "--issue_number", help="issue_number", default=None, required=False
    )
    options = parser.parse_args()
    main(options.github_token, options.repo_name, options.issue_number)
