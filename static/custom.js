; (function () {
  function initTocFab() {
    var toc = document.getElementById("post-toc")
    if (!toc) return
    if (document.querySelector(".post-toc-fab")) return

    toc.classList.add("post-toc-enhanced")

    var tocTitle = toc.querySelector(".post-toc-title")
    if (tocTitle) {
      if (!tocTitle.id) {
        tocTitle.id = "post-toc-title"
      }
      toc.setAttribute("aria-labelledby", tocTitle.id)
    }

    // Create FAB button (icon only)
    var fab = document.createElement("button")
    fab.type = "button"
    fab.className = "post-toc-fab"
    fab.setAttribute("aria-controls", "post-toc")
    fab.setAttribute("aria-expanded", "false")
    fab.setAttribute("aria-label", "切换目录")
    fab.setAttribute("title", "目录")
    fab.innerHTML = '<span class="toc-fab-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg></span>'
    document.body.appendChild(fab)

    var hoverQuery = window.matchMedia("(hover: hover) and (pointer: fine)")
    var closeTimer = null

    function clearCloseTimer() {
      if (closeTimer) {
        clearTimeout(closeTimer)
        closeTimer = null
      }
    }

    function openToc() {
      clearCloseTimer()
      toc.classList.add("is-open")
      fab.classList.add("is-open")
      toc.setAttribute("aria-hidden", "false")
      fab.setAttribute("aria-expanded", "true")
    }

    function closeToc() {
      toc.classList.remove("is-open")
      fab.classList.remove("is-open")
      toc.setAttribute("aria-hidden", "true")
      fab.setAttribute("aria-expanded", "false")
      clearCloseTimer()
    }

    function scheduleCloseToc() {
      clearCloseTimer()
      closeTimer = setTimeout(closeToc, 180)
    }

    // Desktop hover: open on enter, delayed close on leave
    fab.addEventListener("mouseenter", function () {
      if (!hoverQuery.matches) return
      openToc()
    })
    fab.addEventListener("mouseleave", function () {
      if (!hoverQuery.matches) return
      scheduleCloseToc()
    })
    toc.addEventListener("mouseenter", function () {
      if (!hoverQuery.matches) return
      openToc()
    })
    toc.addEventListener("mouseleave", function () {
      if (!hoverQuery.matches) return
      scheduleCloseToc()
    })

    // Click toggle (all devices)
    fab.addEventListener("click", function (event) {
      event.preventDefault()
      event.stopPropagation()
      if (toc.classList.contains("is-open")) {
        closeToc()
      } else {
        openToc()
      }
    })

    // Click outside to close
    document.addEventListener("click", function (event) {
      if (!toc.classList.contains("is-open")) return
      if (toc.contains(event.target) || fab.contains(event.target)) return
      closeToc()
    })

    document.addEventListener("keydown", function (event) {
      if (event.key !== "Escape") return
      if (!toc.classList.contains("is-open")) return
      closeToc()
      fab.focus()
    })

    // TOC link click: close panel (skip on wide screen)
    var wideQuery = window.matchMedia("(min-width: 1560px)")

    toc.querySelectorAll(".toc-link").forEach(function (link) {
      link.addEventListener("click", function () {
        if (wideQuery.matches) return
        if (hoverQuery.matches) {
          scheduleCloseToc()
          return
        }
        closeToc()
      })
    })

    // Wide screen: CSS auto-expands, clean up JS state
    function onWidthChange() {
      if (wideQuery.matches) {
        toc.classList.remove("is-open")
        fab.classList.remove("is-open")
        toc.setAttribute("aria-hidden", "false")
        fab.setAttribute("aria-expanded", "false")
        clearCloseTimer()
      } else {
        toc.setAttribute("aria-hidden", "true")
      }
    }
    if (typeof wideQuery.addEventListener === "function") {
      wideQuery.addEventListener("change", onWidthChange)
    } else if (typeof wideQuery.addListener === "function") {
      wideQuery.addListener(onWidthChange)
    }
    onWidthChange()
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initTocFab)
  } else {
    initTocFab()
  }
})()
