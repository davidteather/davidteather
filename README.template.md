### Hey, I’m David 👋

I’m a software engineer who builds projects that scale, pokes at systems until they break, and enjoys the ride along the way.

🎥 [YouTube](https://www.youtube.com/c/DavidTeatherCodes) | ✍️ [Blog](https://dteather.com/blog/) | 💖 [Sponsor my work](https://github.com/sponsors/davidteather)

---

#### 🚀 Quick Stats
- 🌟 **{{ GITHUB_STARS }}+** GitHub stars  
- 🎓 **{{ LINKEDIN_LEARNERS }}+** learners on [LinkedIn Learning](https://www.linkedin.com/learning/instructors/david-teather)  
- 👁️ **{{ YOUTUBE_SUBSCRIBERS }}+** subscribers | **{{ YOUTUBE_VIEWS }}+** views  

---

#### ✍️ Contact
- 📫 [Email](mailto:contact.davidteather@gmail.com)  
- 🐧 [LinkedIn](https://www.linkedin.com/in/davidteather/)  
- 💖 Support my work on [GitHub Sponsors](https://github.com/sponsors/davidteather), your support helps me keep projects and tutorials free for everyone!  

---

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
