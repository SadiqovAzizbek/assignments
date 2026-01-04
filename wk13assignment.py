import requests

print("Name Age Predictor")

name = input("Enter a name: ").strip().lower()

if not name:
    print("Please enter a name.")
elif not name.isalpha():
    print("Name must contain letters only.")
else:
    try:
        url = "https://api.agify.io"
        response = requests.get(url, params={"name": name})

        if response.status_code != 200:
            print("API error.")
        else:
            data = response.json()

            if data["age"] is None:
                print("No data found for this name.")
            else:
                print("\nResult")
                print("Name:", data["name"].title())
                print("Predicted age:", data["age"])
                print("Count:", data["count"])

                with open("age_prediction.txt", "w") as file:
                    file.write("Name: " + data["name"] + "\n")
                    file.write("Predicted age: " + str(data["age"]) + "\n")
                    file.write("Count: " + str(data["count"]) + "\n")

                print("\nSaved to age_prediction.txt")

    except:
        print("Something went wrong. Check your internet connection.")