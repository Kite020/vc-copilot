def build_state(startup):

    return {

        "startup_name":
        startup["startup_name"],

        "industry":
        startup["industry"],

        "problem":
        startup["problem"],

        "solution":
        startup["solution"],

        "funding_stage":
        "Seed",

        "founders": [
            founder["name"]
            for founder in startup["founders"]
        ]
    }