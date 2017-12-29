from flask import Flask, session, redirect, url_for, request
from flask import render_template
from slat import slat_game
app = Flask(__name__)
                                                                            # IDEA: add a stripping function in the GARDEN
app.jinja_env.add_extension('jinja2.ext.do')
inventory = []
caine_abel = {"killer": 1, "victim": 2, "puzzle_tried": 0}
won = 0
                                                                            # IDEA: make it fool proof
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        action = request.form.get('action')
        if action in slat_game.the_cellar.go_toolbox:
            return redirect(url_for("toolbox"))
        elif action in slat_game.the_cellar.go_shelves:
            return redirect(url_for("shelves"))
        else:
            room = slat_game.the_cellar
            return render_template("cellar.html", room=room)

    else:
        room = slat_game.start
        return render_template("index.html", room=room)

@app.route('/toolbox', methods=['POST', 'GET'])
def toolbox():                                                          # IDEA: wrong return at last step
    room = slat_game.the_toolbox
    if request.method == 'POST':
        action = request.form.get('action')
        if slat_game.the_toolbox.toolboxlist == []:
            inventory.append("hooks")
            if "hooks" in inventory and "fishing rod" in inventory:
                room = slat_game.lines
                inventory.append("lines")
                #slat_game.lines.lines_var = 1
                return render_template("lines.html", room=room, inv=inventory)
            else:
                return redirect(url_for("shelves"))
    return render_template("toolbox.html", room=room, inv=inventory)

@app.route('/shelves', methods=['POST', 'GET'])
def shelves():
    res = slat_game.the_garden
    room = slat_game.the_shelves
    if request.method == 'POST':
        #action = request.form.get('action')
        crates = request.form.get('crates')
        if crates:
            inventory.append("fishing rod")
            if "hooks" in inventory and "fishing rod" in inventory:
                room = slat_game.lines
                inventory.append("lines")
                #slat_game.lines.lines_var = 1
                return render_template("lines.html", room=room, inv=inventory)
            else:
                return redirect(url_for("toolbox"))
    return render_template("shelves.html", room=room, inv=inventory, res=res)

@app.route('/kitchen', methods=['POST', 'GET'])
def kitchen():
    room = slat_game.the_kitchen
    #
    if request.method == 'POST':
        action = request.form.get('action')
        if action in slat_game.the_kitchen.choice_kitchen:
            inventory.append("dog food")
        if 'living' in action:
            return redirect(url_for("living_room"))
        elif action == 'bedroom':
            return redirect(url_for("bedroom"))
    return render_template("kitchen.html", room=room, inv=inventory)

@app.route("/bedroom", methods=['POST', 'GET'])
def bedroom():
    room = slat_game.the_bedroom
    if request.method == 'POST':
        action = request.form.get('action')
        if slat_game.the_bedroom.questions == []:
            return redirect(url_for("hall"))
        elif slat_game.the_bedroom.count >= 7:
            room = slat_game.wife_busted
            return render_template("busted.html", room=room)
        elif slat_game.the_bedroom.love_count == 3:
            love = slat_game.love
            won = 3
            return render_template("busted.html", room=love, won=won)
    return render_template("bedroom.html", room=room, inv=inventory)

@app.route("/living_room", methods=['POST', 'GET'])
def living_room():
    room = slat_game.the_living_room
    if request.method == 'POST':
        action = request.form.get('to_the_hall')
        if action:
            return redirect(url_for("hall"))
    return render_template("living_room.html", room=room, inv=inventory, ca=caine_abel)

@app.route("/hall", methods=['POST', 'GET'])
def hall():
    room = slat_game.the_hall
    if request.method == 'POST':
        action = request.form.get('hall')
        if action:
            return redirect(url_for("garden"))
    return render_template("hall.html", room=room)

@app.route("/garden", methods=['POST', 'GET'])
def garden():                                               #garden temlate is flawed
    room = slat_game.the_garden
    win = slat_game.win
    dawgs = slat_game.dawgs
    if request.method == 'POST':
        action = request.form.get('action')
        if room.passed_garden == 1 and 'dog food' in inventory:
            won = 1
            return render_template("busted.html", room=win, won=won)
        elif room.passed_garden == 1 and 'dog food' not in inventory:
            won = 2
            return render_template("busted.html", room=dawgs, won=won)
    return render_template("garden.html", room=room, inv=inventory)

@app.route("/busted", methods=['POST', 'GET'])
def busted():
    room = slat_game.busted
    if request.method == 'POST':
        #action = request.form.get('action')
        if action:
            return redirect(url_for("index"))
    return render_template("busted.html", room=room)

@app.route("/invent")
def invent ():
    return render_template('inventory.html', inv=inventory)

app.secret_key = "the axiom you can't deny or better"
if __name__ == '__main__':
    app.run(debug=True)
