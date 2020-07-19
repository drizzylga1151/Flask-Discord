from flask import Flask, render_template, redirect, url_for
from flask_discord import DiscordOAuth2Session, requires_authorization, Unauthorized

app = Flask(__name__)

app.secret_key = b"Random bytes flask secret"

app.config["DEBUG"] = True
app.config["DISCORD_CLIENT_ID"] = 
app.config["DISCORD_CLIENT_SECRET"] = "" 
app.config["DISCORD_REDIRECT_URI"] = "https://localhost/callback/"  

discord = DiscordOAuth2Session(app)

@app.route("/")
def main():
    
    return discord.create_session()

@app.route("/callback/")
def cb():
    discord.callback()
    return redirect(url_for("dash"))

@app.route("/dash")
@requires_authorization
def dash():

    self = discord.fetch_user()

    gud = self.fetch_guilds()

    selfguilds=[]

    for guild in gud:
        selfguilds.append(guild.name)

    return render_template('dash.html', user=self, guilds=selfguilds)

app.run('localhost', 443, ssl_context='adhoc')
