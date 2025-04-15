from wisdom_nuggets.app import create_app

app = create_app()

if __name__ == "__main__":
    print("\n🚀 Wisdom Nuggets API is running!")
    print("📌 Visit these endpoints:")
    print("   → GET all nuggets:     http://127.0.0.1:5000/nuggets")
    print("   → GET random nugget:   http://127.0.0.1:5000/nuggets/random")
    print("   → POST new nugget:     http://127.0.0.1:5000/nuggets")
    print("   → DELETE a nugget:     http://127.0.0.1:5000/nuggets/<id>\n")

    app.run(debug=True)
