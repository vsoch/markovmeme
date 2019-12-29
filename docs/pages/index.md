---
layout: default
permalink: /
---

<div class="container">
   <h1 class="heading">Gallery</h1>
     <p>Yes, these are terrible</p>
     <div class="gallery">
       <div class="gallery-item">
{% for image in site.static_files %}{% if image.path contains 'assets/gallery/' %}<div class="gallery-item">
<img class="gallery-image" src="{{ site.baseurl }}{{ image.path }}" alt="">
</div>{% endif %}{% endfor %}
  </div>
</div>
