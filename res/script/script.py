from res.transactions import Transaction

option = True
material_confirmation = True


print("Welcome to the app")

while option:
    while material_confirmation:
        print("Are you recycling glass or aluminum?")
        material = input()
        material = material.lower()

        if material == 'glass' or material == 'aluminum':
            material_confirmation = False
        else:
            print("Your material isn't part of the list. Please try again")

    print("How much does it weight? (On kilograms)")
    weight = input()
    if material == 'glass':
        weight = int(weight)4
        def post(self):
        _id = str(database.db.transaction.insert_one({
                "glass": request.json["glass"],
                "aluminum": request.json["aluminum"],
                "username": request.json["username"],
                "machine": request.json["machine"]
        }).inserted_id)

        return _id

    else:
        weight = int(weight)2
        transaction = jsonify({
                            "glass":"0",
                            "aluminum":material,
                            "username":"Enoch",
                            "machine":"1"})