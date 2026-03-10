def dashboard(data):

    print("\n")
    print("╔════════════════════════════╗")
    print("        DEV PULSE REPORT")
    print("╚════════════════════════════╝")

    print("\n📊 Languages\n")

    max_value = max(data["languages"].values())

    for lang,value in data["languages"].items():

        bar = "█" * int((value/max_value)*20)

        print(f"{lang:<12} {bar} {value}")

    print("\n🧠 Complexity Score:",data["complexity"])

    print("📝 TODO count:",data["todos"])

    print("\n📂 Largest File:")
    print(data["largest_file"][0],"(",data["largest_file"][1],"lines )")

    print("\nProject Health:")

    health = max(0,100 - data["complexity"])

    bar = "█" * int(health/5)

    print(f"{health}/100 {bar}")

    print("\n")
    
def dashboard(result):
    print("\nProject Dashboard")
    print("-----------------")

    print(f"Total Files: {result['total_files']}")

    print("\nLanguages:")
    for lang, count in result["languages"].items():
        print(f"{lang}: {count}")

    print(f"\nTODO comments: {result['todos']}")