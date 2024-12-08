---
title: Contact
nav:
  order: 5
  tooltip: Email, address, and location
---

# {% include icon.html icon="fa-regular fa-envelope" %}Contact

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

{%
  include button.html
  type="email"
  text="ao3014@hunter.cuny.edu"
  link="ao3014@hunter.cuny.edu"
%}

{%
  include button.html
  type="address"
  tooltip="Our location on Google Maps for easy navigation"
  link="https://g.co/kgs/GHvw54k"
%}

{% include section.html %}

{% capture col1 %}

{%
  include figure.html
  image="images/huntercollege.jpg"
  caption="Street view of Hunter!"
%}

{% endcapture %}

{% include cols.html col1=col1 %}

{% include section.html dark=true %}
