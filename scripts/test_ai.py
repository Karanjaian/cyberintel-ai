from app.ai.summarizer import summarize

article = """
Cisco has released security updates addressing a critical vulnerability
that allows remote attackers to gain root access on affected SD-WAN devices.
"""

summary = summarize(article)

print("\nGenerated Summary:\n")
print(summary)
