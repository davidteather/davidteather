### Hi there 👋
- 💡 Software engineer, content creator, and much more 😄
- ✍️ [Blogging](https://dteather.com/blog/) about things I'm doing, learning, tech tutorials, and more
- 🔭 Currently creating an [open source evenet management platform](https://github.com/ApplicantAtlas/ApplicantAtlas) focused on hackathons
- 🎥 Making tech content on the [David Teather Codes](https://www.youtube.com/c/DavidTeatherCodes) YouTube channel
- 💖 Join the **{{ GITHUB_SPONSORS }}** people who have [sponsored me](https://github.com/sponsors/davidteather), which enables me to create more free content and tools!

#### 🚀 Quick Stats
- 🌟 **{{ GITHUB_STARS }}+** stars on GitHub
- 🎓 Guided **{{ LINKEDIN_LEARNERS }}+** learners on my [LinkedIn Learning courses](https://www.linkedin.com/learning/instructors/david-teather)
- 👁️ Over **{{ YOUTUBE_SUBSCRIBERS }}+** subscribers, and **{{ YOUTUBE_VIEWS }}+** views on YouTube

#### ✍️ Contact Me
- 📫 Feel free to shoot me an email at [contact.davidteather@gmail.com](mailto:contact.davidteather@gmail.com) for any inquiries
- 🐧 Let's connect on [LinkedIn](https://www.linkedin.com/in/davidteather/).

#### 📰 Latest Content
<table><tr>
{% for category, articles in RSS.items() %}
<td valign="top" width="{{ 100 // RSS|length }}%">

### Recent {{ category }}
{% for article in articles %}
- [{{ article.title }}]({{ article.link }}) - {{ article.published }}
{% endfor %}
</td>
{% endfor %}
</tr></table>
