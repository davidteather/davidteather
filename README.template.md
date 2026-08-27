### Hey, I’m David 👋

I’m a software engineer who builds projects that scale, pokes at systems until they break, and enjoys the ride along the way.

🎥 [YouTube](https://go.dteather.com/youtube?src=github&placement=nav) | ✍️ [Blog](https://go.dteather.com/blog?src=github&placement=nav) | 💖 [Sponsor my work](https://go.dteather.com/github-sponsors?src=github&placement=nav)

#### 🚀 Quick Stats
- 🌟 **{{ GITHUB_STARS }}+** GitHub stars  
- 🎓 **{{ LINKEDIN_LEARNERS }}+** learners on [LinkedIn Learning](https://go.dteather.com/linkedin-learning?src=github&placement=nav)  
- 👁️ **{{ YOUTUBE_SUBSCRIBERS }}+** subscribers | **{{ YOUTUBE_VIEWS }}+** views  

#### ✍️ Contact
- 📫 [Email](mailto:contact.davidteather@gmail.com)  
- 🐧 [LinkedIn](https://go.dteather.com/linkedin?src=github&placement=contact)  
- 💖 Support my work on [GitHub Sponsors](https://go.dteather.com/github-sponsors?src=github&placement=contact), your support helps me keep projects and tutorials free for everyone!  

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
