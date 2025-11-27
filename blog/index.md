--- 
title: Blog
nav:
  order: 4
  tooltip: Writings
---

# {% include icon.html icon="fa-solid fa-feather-pointed" %}Blog

<div style="text-align: center;">
Stay up to date with our lab!
</div>

{% include section.html %}

{% include search-box.html %}

{% include tags.html tags=site.tags %}

{% include search-info.html %}

{% include list.html data="posts" component="post-excerpt" %}
