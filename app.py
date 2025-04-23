from flask import Flask, render_template, redirect, url_for
from system import Player, OmniDimensionSystem
import data

app = Flask(__name__)
player = Player(name="Ký Chủ", rank=data.sample_character().rank)
for _ in range(3):
    player.characters.append(data.sample_character())
sys = OmniDimensionSystem(player)

@app.route("/")
def index():
    return render_template("index.html", player=player, log=player.log_history[::-1])

@app.route("/action/<act>")
def do_action(act):
    if act == "gacha":
        sys.spin_gacha()
    elif act == "quest":
        sys.accept_quest(data.sample_quest())
    elif act == "travel":
        sys.travel_dimension()
    elif act == "shard":
        sys.collect_shard()
    elif act == "upgrade":
        sys.upgrade_system()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)