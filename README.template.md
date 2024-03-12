### Hi there 👋
- 💡 Software engineer, student, content creator, and much more 😄
- 🔭 Currently crafting a comprehensive resource for [everything web scraping](https://github.com/davidteather/everything-web-scraping)
- 🎥 Making tech content on the [David Teather](https://www.youtube.com/c/davidteather?sub_confirmation=1), and [David Teather Codes channel](https://www.youtube.com/c/DavidTeatherCodes?sub_confirmation=1) YouTube channels
- ✍️ Blogging about privacy and security on [The Response Times](https://theresponsetimes.com)
- 💖 Join the **{{ GITHUB_SPONSORS }}** people [sponsoring me](https://github.com/sponsors/davidteather), enabling me to create more free content and tools!

#### 🚀 Quick Stats
- 🌟 **{{ GITHUB_STARS }}+** stars on GitHub
- 🎓 Guided **{{ LINKEDIN_LEARNERS }}+** learners on my [LinkedIn Learning courses](https://www.linkedin.com/learning/instructors/david-teather)
- 👁️ Over **{{ YOUTUBE_SUBSCRIBERS }}+** subscribers, and **{{ YOUTUBE_VIEWS }}+** views on YouTube

#### ✍️ Contact Me
- 📫 Feel free to shoot me an email at [contact.davidteather@gmail.com](mailto:contact.davidteather@gmail.com) for any inquiries
- 🐧 Let's connect on [LinkedIn](https://www.linkedin.com/in/davidteather/).

#### 📰 Latest Content
<div style="display: flex; flex-wrap: wrap;">
{% for category, articles in RSS.items() %}
<div style="flex: 1; min-width: calc({{ WIDTH_PERCENTAGE }}% - 20px); max-width: calc({{ WIDTH_PERCENTAGE }}% - 20px); margin: 10px;">
<h3>{{ category }}</h3>
{% for article in articles %}
<div>
<a href="{{ article.link }}" target="_blank">{{ article.title }}</a>
<p>Published: {{ article.published }}</p>
</div>
{% endfor %}
</div>
{% endfor %}
</div>