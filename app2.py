import streamlit as st
import random

# Step 1: Define image-question mapping
image_question_map = {
    "Pop.jpg": [("What kind of energy are you looking for right now?", ["🍭 Bursty & bold", "🧊 Cool and refreshing", "🍇 Fruity & fun", "🥛 Something chill to mellow down"]), 
                    ("What form do you feel like?", ["🥤 A drink", "🥄 A scoop or bite", "🍡 Finger-snack or chewable", "❌ Not sure — surprise me"])],
    "lofi.jpg": [("Want to stay in this focused flow or feel a little refreshed?", ["🧠 Stay focused", "🔁 Shift a bit — light refresh", "😌 Slight uplift", "🌬️ Doesn’t matter — just keep it light"]), 
                    ("What kind of texture feels right?", ["🧊 Cold and smooth", "🍵 Room-temp and gentle", "🍪 Lightly crunchy", "🥣 Soft and creamy"])],
    "Acoustic.jpg": [("What would feel best right now?", ["🌡️ Something warm and comforting", "🧊 Cool but cozy", "🫗 A soft sip", "🥣 A mellow bite"]), 
                    ("Do you want flavor that’s:", ["🌿 Mild & soothing", "🍋 Tangy or refreshing", "🍭 Sweet but soft", "❌ I trust you — pick for me"])],
    "hip hop.jpg": [("What helps you stay in this mode?", ["🚀 A quick energy push", "🥤 Something zesty or fizzy", "🧃 Clean refreshment", "🍪 A bold, strong snack"]), 
                    ("Do you want something:", ["🧊 Cold & sharp", "🥣 Room temp & satisfying", "💥 With a punch of flavor", "🧘 Subtle but grounding"])],
    "turn it up_glow.png": [("How would you keep the glow going?", ["🍇 Fruity refresh", "🍦 Sweet & soft", "🧊 Mild cool sip", "🌸 Something gentle"]), 
                    ("What temperature feels best?", ["🧊 Cold", "🥣 Room temp", "🌡️ Slightly warm", "❓ Anything mellow"])],
    "in my zone_melt.png": [("Looking for comfort or emotional ease?", ["🌡️ Warm & soft", "🍚 Creamy & mild", "🍫 Sweet hug", "☁️ Let it melt me"]), 
                    ("What type of food feels safe now?", ["🥣 Smooth bite", "🧃 Calm sip", "🍪 Familiar texture", "❌ I’m okay with anything soft"])],
    "stay in_storm.png": [("Want to ground yourself or escape a little?", ["🌱 Ground me", "🍋 Lift me lightly", "🧊 Cool me down", "❓ Whatever helps settle"]), 
                    ("What sensation fits this moment?", ["🥤 Clean & cold", "🍽️ Strong bite", "🧘 Gentle & smooth", "🥣 Tangy balance"])],
    "flow state_snap.png": [("Do you need something to keep you locked in?", ["💥 Bold fuel", "🧊 Cool clarity", "🥤 Crisp refresh", "❓ Doesn’t matter — keep me sharp"]), 
                    ("Do you need something to keep you locked in?", ["🍫 Flavor burst", "🥤 Drinkable focus", "🍪 Crunchy confidence", "🥣 Balanced & steady"])],
    "feel good_float.png": [("Want to stay floating or softly touch ground?", ["🌫 Stay floaty", "🍃 Gentle grounding", "🧊 Light refresh", "❓ Don’t know — surprise me"]), 
                    ("What form do you prefer?", ["🥣 Soft spoon snack", "🍸 Sip-sized calm", "🍦 Creamy & light", "❌ Any vibe-friendly treat"])],
    "rock out_Bounce.png": [("Want to keep bouncing or slow it slightly?", ["🎉 Keep bouncing!", "🌙 Slow bounce", "🍉 Chill pop", "❓ Anything playful"]), 
                     ("Your snack mood now?", ["🥤 Cold & fizzy", "🍓 Fruity burst", "🍪 Sweet & fun", "🍬 Chewable joy"])],
    "sentimental_grounded.png": [("What kind of balance feels right?", ["🌿 Herbal/mild", "🍚 Neutral bite", "🥤 Clean sip", "❓ Just keep it simple"]), 
                     ("Craving a format that's…", ["🥣 Room temp", "🧃 Cold & clear", "🧘 Smooth & plain", "🍽️ Familiar & filling"])],
    "sing along_rise.png": [("Want a small push or full boost?", ["🔋 Just a nudge", "🚀 Full throttle", "🥤 Clean uplift", "❓ Anything functional"]), 
                     ("Pick a format that helps power you:", ["🥤 Cold refresh", "🍪 Energizing bite", "🍯 Protein+comfort", "🥚 Fuel me fast"])]
}

# Step 2: Define recommendations based on option selection
recommendations_dict = {
    "flow state_snap.png": {
        "recommendations": {
            ("Sharp & focused", "Zingy kick"): ["Taaza Jeera", "Eggs", "Sweet Corn"],
            ("Sharp & focused", "Cool energy"): ["Coconut Water", "Strawberry Yogurt", "Fruits"],
            ("Sharp & focused", "Soft chew"): ["Curd", "Sweet Corn", "Mango Yogurt"],
            ("Sharp & focused", "Classic calm"): ["Milk", "Curd", "Fruits"],
            ("Introspective", "Zingy kick"): ["Pudina Chaach", "Soups", "Curd"],
            ("Introspective", "Cool energy"): ["Coconut Water", "Fruits", "Blueberry Yogurt"],
            ("Introspective", "Soft chew"): ["Sweet Corn", "Eggs", "Curd"],
            ("Introspective", "Classic calm"): ["Milk", "Curd", "Taaza Jeera"],
            ("Fast-paced", "Zingy kick"): ["Taaza Jeera", "Soups", "Mango Yogurt"],
            ("Fast-paced", "Cool energy"): ["Coconut Water", "Mango Lassi", "Strawberry Yogurt"],
            ("Fast-paced", "Soft chew"): ["Sweet Corn", "Curd", "Eggs"],
            ("Fast-paced", "Classic calm"): ["Milk", "Curd", "Fruits"],
            ("Surprise me", "Zingy kick"): ["Taaza Jeera", "Eggs", "Soups"],
            ("Surprise me", "Cool energy"): ["Coconut Water", "Mango Lassi", "Blueberry Yogurt"],
            ("Surprise me", "Soft chew"): ["Curd", "Fruits", "Sweet Corn"],
            ("Surprise me", "Classic calm"): ["Milk", "Curd", "Mango Yogurt"]
        }
    },
    "rock out_Bounce.png": {
        "recommendations": {
            ("Bubbly & active", "Juicy pop"): ["Mango Lassi", "Coconut Water", "Fruits"],
            ("Bubbly & active", "Crunchy boost"): ["Eggs", "Sweet Corn", "Fruits"],
            ("Bubbly & active", "Creamy joy"): ["Mango Yogurt", "Blueberry Yogurt", "Curd"],
            ("Bubbly & active", "Chill vibe"): ["Strawberry Yogurt", "Coconut Water", "Milk"],
            ("Playful", "Juicy pop"): ["Strawberry Yogurt", "Mango Lassi", "Fruits"],
            ("Playful", "Crunchy boost"): ["Sweet Corn", "Eggs", "Curd"],
            ("Playful", "Creamy joy"): ["Mango Yogurt", "Curd", "Blueberry Yogurt"],
            ("Playful", "Chill vibe"): ["Coconut Water", "Milk", "Taaza Jeera"],
            ("Uplifted calm", "Juicy pop"): ["Coconut Water", "Strawberry Yogurt", "Mango Lassi"],
            ("Uplifted calm", "Crunchy boost"): ["Eggs", "Sweet Corn", "Fruits"],
            ("Uplifted calm", "Creamy joy"): ["Blueberry Yogurt", "Curd", "Mango Yogurt"],
            ("Uplifted calm", "Chill vibe"): ["Milk", "Coconut Water", "Curd"],
            ("Surprise me", "Juicy pop"): ["Mango Lassi", "Blueberry Yogurt", "Fruits"],
            ("Surprise me", "Crunchy boost"): ["Sweet Corn", "Eggs", "Curd"],
            ("Surprise me", "Creamy joy"): ["Strawberry Yogurt", "Curd", "Mango Yogurt"],
            ("Surprise me", "Chill vibe"): ["Coconut Water", "Milk", "Taaza Jeera"]
        }
    },

    "feel good_float.png": {
        "recommendations": {
            ("Light & airy", "Cool hydration"): ["Coconut Water", "Mango Lassi", "Strawberry Yogurt"],
            ("Light & airy", "Subtle sweetness"): ["Mango Yogurt", "Blueberry Yogurt", "Curd"],
            ("Light & airy", "Smooth neutral"): ["Milk", "Curd", "Coconut Water"],
            ("Light & airy", "Mild crunch"): ["Sweet Corn", "Fruits", "Eggs"],
            ("Deep & still", "Cool hydration"): ["Taaza Jeera", "Pudina Masala Chaach", "Coconut Water"],
            ("Deep & still", "Subtle sweetness"): ["Strawberry Yogurt", "Mango Lassi", "Curd"],
            ("Deep & still", "Smooth neutral"): ["Curd", "Mango Yogurt", "Milk"],
            ("Deep & still", "Mild crunch"): ["Sweet Corn", "Eggs", "Fruits"],
            ("Free & curious", "Cool hydration"): ["Coconut Water", "Blueberry Yogurt", "Taaza Jeera"],
            ("Free & curious", "Subtle sweetness"): ["Mango Yogurt", "Curd", "Strawberry Yogurt"],
            ("Free & curious", "Smooth neutral"): ["Milk", "Coconut Water", "Curd"],
            ("Free & curious", "Mild crunch"): ["Fruits", "Sweet Corn", "Eggs"],
            ("Surprise me", "Cool hydration"): ["Mango Lassi", "Coconut Water", "Curd"],
            ("Surprise me", "Subtle sweetness"): ["Blueberry Yogurt", "Strawberry Yogurt", "Mango Yogurt"],
            ("Surprise me", "Smooth neutral"): ["Milk", "Curd", "Coconut Water"],
            ("Surprise me", "Mild crunch"): ["Eggs", "Sweet Corn", "Fruits"]
        }
    },

    "stay in_storm.png": {
        "recommendations": {
            ("Restless", "Cold & crisp"): ["Coconut Water", "Mango Lassi", "Curd"],
            ("Restless", "Spicy & warm"): ["Soups", "Pudina Chaach", "Milk"],
            ("Restless", "Soothing & soft"): ["Curd", "Strawberry Yogurt", "Sweet Corn"],
            ("Restless", "Simple classic"): ["Milk", "Sweet Corn", "Fruits"],
            ("Explosive", "Cold & crisp"): ["Taaza Jeera", "Coconut Water", "Strawberry Yogurt"],
            ("Explosive", "Spicy & warm"): ["Soups", "Eggs", "Mango Lassi"],
            ("Explosive", "Soothing & soft"): ["Blueberry Yogurt", "Curd", "Sweet Corn"],
            ("Explosive", "Simple classic"): ["Milk", "Fruits", "Mango Yogurt"],
            ("Tense but sharp", "Cold & crisp"): ["Pudina Chaach", "Mango Lassi", "Coconut Water"],
            ("Tense but sharp", "Spicy & warm"): ["Soups", "Taaza Jeera", "Curd"],
            ("Tense but sharp", "Soothing & soft"): ["Curd", "Sweet Corn", "Mango Yogurt"],
            ("Tense but sharp", "Simple classic"): ["Fruits", "Milk", "Curd"],
            ("Surprise me", "Cold & crisp"): ["Coconut Water", "Mango Lassi", "Taaza Jeera"],
            ("Surprise me", "Spicy & warm"): ["Soups", "Pudina Chaach", "Milk"],
            ("Surprise me", "Soothing & soft"): ["Curd", "Blueberry Yogurt", "Mango Yogurt"],
            ("Surprise me", "Simple classic"): ["Milk", "Sweet Corn", "Fruits"]
        }
    },
    "in my zone_melt.png": {
        "recommendations": {
            ("Still & soft", "Creamy comfort"): ["Curd", "Mango Yogurt", "Sweet Corn"],
            ("Still & soft", "Gentle sip"): ["Milk", "Taaza Jeera", "Coconut Water"],
            ("Still & soft", "Simple chew"): ["Fruits", "Sweet Corn", "Eggs"],
            ("Still & soft", "Ambient cool"): ["Coconut Water", "Blueberry Yogurt", "Curd"],
            ("Heavy & slow", "Creamy comfort"): ["Curd", "Strawberry Yogurt", "Sweet Corn"],
            ("Heavy & slow", "Gentle sip"): ["Milk", "Pudina Masala Chaach", "Coconut Water"],
            ("Heavy & slow", "Simple chew"): ["Eggs", "Sweet Corn", "Fruits"],
            ("Heavy & slow", "Ambient cool"): ["Coconut Water", "Curd", "Mango Lassi"],
            ("Dreamy flow", "Creamy comfort"): ["Mango Yogurt", "Curd", "Strawberry Yogurt"],
            ("Dreamy flow", "Gentle sip"): ["Coconut Water", "Milk", "Taaza Jeera"],
            ("Dreamy flow", "Simple chew"): ["Sweet Corn", "Eggs", "Fruits"],
            ("Dreamy flow", "Ambient cool"): ["Mango Lassi", "Curd", "Coconut Water"],
            ("Surprise me", "Creamy comfort"): ["Blueberry Yogurt", "Curd", "Sweet Corn"],
            ("Surprise me", "Gentle sip"): ["Milk", "Pudina Chaach", "Coconut Water"],
            ("Surprise me", "Simple chew"): ["Eggs", "Sweet Corn", "Fruits"],
            ("Surprise me", "Ambient cool"): ["Strawberry Yogurt", "Mango Lassi", "Curd"]
        }
    },
    "sentimental_grounded.png": {
        "recommendations": {
            ("Rooted & centered", "Warm sip"): ["Milk", "Soups", "Pudina Chaach"],
            ("Rooted & centered", "Subtle sweetness"): ["Curd", "Mango Yogurt", "Strawberry Yogurt"],
            ("Rooted & centered", "Neutral bite"): ["Eggs", "Sweet Corn", "Curd"],
            ("Rooted & centered", "Traditional comfort"): ["Curd", "Fruits", "Milk"],
            ("Still & quiet", "Warm sip"): ["Soups", "Milk", "Taaza Jeera"],
            ("Still & quiet", "Subtle sweetness"): ["Blueberry Yogurt", "Mango Yogurt", "Curd"],
            ("Still & quiet", "Neutral bite"): ["Fruits", "Sweet Corn", "Curd"],
            ("Still & quiet", "Traditional comfort"): ["Milk", "Curd", "Pudina Chaach"],
            ("Stable & light", "Warm sip"): ["Pudina Chaach", "Milk", "Soups"],
            ("Stable & light", "Subtle sweetness"): ["Mango Yogurt", "Strawberry Yogurt", "Curd"],
            ("Stable & light", "Neutral bite"): ["Sweet Corn", "Fruits", "Curd"],
            ("Stable & light", "Traditional comfort"): ["Eggs", "Milk", "Curd"],
            ("Surprise me", "Warm sip"): ["Soups", "Pudina Chaach", "Milk"],
            ("Surprise me", "Subtle sweetness"): ["Strawberry Yogurt", "Mango Yogurt", "Curd"],
            ("Surprise me", "Neutral bite"): ["Eggs", "Fruits", "Sweet Corn"],
            ("Surprise me", "Traditional comfort"): ["Milk", "Curd", "Coconut Water"]
        }
    },

    "sing along_rise.png": {
        "recommendations": {
            ("Focused & ready", "Light energy"): ["Coconut Water", "Fruits", "Strawberry Yogurt"],
            ("Focused & ready", "Balanced bite"): ["Curd", "Sweet Corn", "Eggs"],
            ("Focused & ready", "Bold flavor"): ["Taaza Jeera", "Pudina Chaach", "Mango Yogurt"],
            ("Focused & ready", "Steady sip"): ["Milk", "Curd", "Mango Lassi"],
            ("Hopeful", "Light energy"): ["Mango Lassi", "Fruits", "Curd"],
            ("Hopeful", "Balanced bite"): ["Eggs", "Sweet Corn", "Curd"],
            ("Hopeful", "Bold flavor"): ["Pudina Chaach", "Taaza Jeera", "Strawberry Yogurt"],
            ("Hopeful", "Steady sip"): ["Milk", "Mango Yogurt", "Coconut Water"],
            ("Motivated chill", "Light energy"): ["Coconut Water", "Mango Lassi", "Blueberry Yogurt"],
            ("Motivated chill", "Balanced bite"): ["Sweet Corn", "Fruits", "Eggs"],
            ("Motivated chill", "Bold flavor"): ["Taaza Jeera", "Soups", "Pudina Chaach"],
            ("Motivated chill", "Steady sip"): ["Milk", "Curd", "Strawberry Yogurt"],
            ("Surprise me", "Light energy"): ["Coconut Water", "Mango Lassi", "Fruits"],
            ("Surprise me", "Balanced bite"): ["Curd", "Eggs", "Sweet Corn"],
            ("Surprise me", "Bold flavor"): ["Pudina Chaach", "Taaza Jeera", "Mango Yogurt"],
            ("Surprise me", "Steady sip"): ["Milk", "Curd", "Blueberry Yogurt"]
        }
    },

    "turn it up_glow.png": {
        "recommendations": {
            ("Bright & zesty", "Chilled & fruity"): ["Coconut Water", "Mango Lassi", "Strawberry Yogurt"],
            ("Bright & zesty", "Smooth & mild"): ["Mango Yogurt", "Curd", "Blueberry Yogurt"],
            ("Bright & zesty", "Chewy & familiar"): ["Sweet Corn", "Fruits", "Curd"],
            ("Bright & zesty", "Delicate touch"): ["Milk", "Curd", "Coconut Water"],
            ("Peaceful joy", "Chilled & fruity"): ["Mango Lassi", "Coconut Water", "Fruits"],
            ("Peaceful joy", "Smooth & mild"): ["Curd", "Blueberry Yogurt", "Mango Yogurt"],
            ("Peaceful joy", "Chewy & familiar"): ["Sweet Corn", "Eggs", "Fruits"],
            ("Peaceful joy", "Delicate touch"): ["Milk", "Curd", "Strawberry Yogurt"],
            ("Soft & happy", "Chilled & fruity"): ["Coconut Water", "Strawberry Yogurt", "Fruits"],
            ("Soft & happy", "Smooth & mild"): ["Blueberry Yogurt", "Curd", "Mango Yogurt"],
            ("Soft & happy", "Chewy & familiar"): ["Sweet Corn", "Eggs", "Curd"],
            ("Soft & happy", "Delicate touch"): ["Milk", "Fruits", "Coconut Water"],
            ("Surprise me", "Chilled & fruity"): ["Mango Lassi", "Coconut Water", "Blueberry Yogurt"],
            ("Surprise me", "Smooth & mild"): ["Curd", "Strawberry Yogurt", "Milk"],
            ("Surprise me", "Chewy & familiar"): ["Fruits", "Sweet Corn", "Curd"],
            ("Surprise me", "Delicate touch"): ["Milk", "Coconut Water", "Mango Yogurt"]
        }
    },
    "Pop.jpg": {
        "recommendations": {
            ("Fruity fun", "Drink"): ["Mango Lassi", "Coconut Water", "Strawberry Yogurt"],
            ("Fruity fun", "Snack"): ["Mango Yogurt", "Sweet Corn", "Strawberry Yogurt"],
            ("Fruity fun", "Soft"): ["Mango Yogurt", "Fruits", "Sweet Corn"],
            ("Fruity fun", "Surprise"): ["Mango Lassi", "Curd", "Fruits"],
            ("Cold & fizzy", "Drink"): ["Taaza Jeera Chaach", "Pudina Masala Chaach", "Coconut Water"],
            ("Cold & fizzy", "Snack"): ["Sweet Corn", "Curd", "Fruits"],
            ("Cold & fizzy", "Soft"): ["Pudina Masala Chaach", "Mango Yogurt", "Coconut Water"],
            ("Cold & fizzy", "Surprise"): ["Taaza Jeera Chaach", "Mango Lassi", "Blueberry Yogurt"],
            ("Sweet blast", "Drink"): ["Mango Lassi", "Blueberry Yogurt", "Strawberry Yogurt"],
            ("Sweet blast", "Snack"): ["Strawberry Yogurt", "Mango Yogurt", "Curd"],
            ("Sweet blast", "Soft"): ["Curd", "Mango Yogurt", "Sweet Corn"],
            ("Sweet blast", "Surprise"): ["Strawberry Yogurt", "Sweet Corn", "Milk"],
            ("Light but exciting", "Drink"): ["Coconut Water", "Pudina Masala Chaach", "Milk"],
            ("Light but exciting", "Snack"): ["Sweet Corn", "Fruits", "Mango Yogurt"],
            ("Light but exciting", "Soft"): ["Curd", "Fruits", "Coconut Water"],
            ("Light but exciting", "Surprise"): ["Coconut Water", "Taaza Jeera Chaach", "Strawberry Yogurt"]
        }
    },
    "Acoustic.jpg": {
        "recommendations": {
            ("Warm & comfy", "Hot & sip-worthy"): ["Soups", "Pudina Masala Chaach", "Milk"],
            ("Warm & comfy", "Creamy & soft"): ["Curd", "Blueberry Yogurt", "Sweet Corn"],
            ("Warm & comfy", "Familiar bite"): ["Eggs", "Sweet Corn", "Curd"],
            ("Warm & comfy", "Neutral pick"): ["Curd", "Milk", "Mango Yogurt"],
            ("Mild & easy", "Hot & sip-worthy"): ["Soups", "Mango Lassi", "Taaza Jeera Chaach"],
            ("Mild & easy", "Creamy & soft"): ["Curd", "Strawberry Yogurt", "Coconut Water"],
            ("Mild & easy", "Familiar bite"): ["Sweet Corn", "Fruits", "Curd"],
            ("Mild & easy", "Neutral pick"): ["Fruits", "Milk", "Coconut Water"],
            ("Relaxed but alert", "Hot & sip-worthy"): ["Pudina Masala Chaach", "Taaza Jeera", "Soups"],
            ("Relaxed but alert", "Creamy & soft"): ["Curd", "Mango Yogurt", "Sweet Corn"],
            ("Relaxed but alert", "Familiar bite"): ["Eggs", "Fruits", "Curd"],
            ("Relaxed but alert", "Neutral pick"): ["Milk", "Sweet Corn", "Mango Lassi"],
            ("Surprise me", "Hot & sip-worthy"): ["Soups", "Pudina Masala Chaach", "Milk"],
            ("Surprise me", "Creamy & soft"): ["Mango Yogurt", "Curd", "Blueberry Yogurt"],
            ("Surprise me", "Familiar bite"): ["Fruits", "Eggs", "Sweet Corn"],
            ("Surprise me", "Neutral pick"): ["Milk", "Coconut Water", "Mango Lassi"]
        }
    },

    "hip hop.jpg": {
        "recommendations": {
            ("Hyped & loud", "Cold & bold"): ["Mango Lassi", "Taaza Jeera Chaach", "Coconut Water"],
            ("Hyped & loud", "Crunchy edge"): ["Eggs", "Fruits", "Sweet Corn"],
            ("Hyped & loud", "Soft balance"): ["Strawberry Yogurt", "Curd", "Coconut Water"],
            ("Hyped & loud", "Classic fix"): ["Milk", "Fruits", "Sweet Corn"],
            ("Bold & sharp", "Cold & bold"): ["Taaza Jeera Chaach", "Pudina Masala Chaach", "Mango Yogurt"],
            ("Bold & sharp", "Crunchy edge"): ["Sweet Corn", "Eggs", "Curd"],
            ("Bold & sharp", "Soft balance"): ["Curd", "Blueberry Yogurt", "Mango Lassi"],
            ("Bold & sharp", "Classic fix"): ["Fruits", "Milk", "Coconut Water"],
            ("Confident calm", "Cold & bold"): ["Coconut Water", "Mango Lassi", "Taaza Jeera"],
            ("Confident calm", "Crunchy edge"): ["Sweet Corn", "Eggs", "Curd"],
            ("Confident calm", "Soft balance"): ["Curd", "Blueberry Yogurt", "Sweet Corn"],
            ("Confident calm", "Classic fix"): ["Fruits", "Milk", "Mango Yogurt"],
            ("Surprise me", "Cold & bold"): ["Coconut Water", "Mango Lassi", "Pudina Chaach"],
            ("Surprise me", "Crunchy edge"): ["Sweet Corn", "Eggs", "Curd"],
            ("Surprise me", "Soft balance"): ["Curd", "Mango Yogurt", "Blueberry Yogurt"],
            ("Surprise me", "Classic fix"): ["Milk", "Fruits", "Mango Lassi"]
        }
    },

    "lofi.jpg": {
        "recommendations": {
            ("Stay in flow", "Cool & creamy"): ["Coconut Water", "Mango Yogurt", "Eggs"],
            ("Stay in flow", "Room-temp"): ["Curd", "Coconut Water", "Sweet Corn"],
            ("Stay in flow", "Smooth"): ["Blueberry Yogurt", "Milk", "Curd"],
            ("Stay in flow", "Crunchy"): ["Fruits", "Sweet Corn", "Taaza Jeera Chaach"],
            ("Light refresh", "Cool & creamy"): ["Strawberry Yogurt", "Coconut Water", "Mango Lassi"],
            ("Light refresh", "Room-temp"): ["Pudina Masala Chaach", "Curd", "Sweet Corn"],
            ("Light refresh", "Smooth"): ["Milk", "Mango Yogurt", "Fruits"],
            ("Light refresh", "Crunchy"): ["Eggs", "Fruits", "Mango Lassi"],
            ("Gentle uplift", "Cool & creamy"): ["Mango Yogurt", "Eggs", "Coconut Water"],
            ("Gentle uplift", "Room-temp"): ["Milk", "Sweet Corn", "Mango Lassi"],
            ("Gentle uplift", "Smooth"): ["Curd", "Coconut Water", "Blueberry Yogurt"],
            ("Gentle uplift", "Crunchy"): ["Fruits", "Corn", "Pudina Chaach"],
            ("Surprise me", "Cool & creamy"): ["Strawberry Yogurt", "Curd", "Mango Lassi"],
            ("Surprise me", "Room-temp"): ["Milk", "Sweet Corn", "Fruits"],
            ("Surprise me", "Smooth"): ["Mango Yogurt", "Coconut Water", "Curd"],
            ("Surprise me", "Crunchy"): ["Sweet Corn", "Taaza Jeera", "Fruits"]
        }
    }
}


st.set_page_config(page_title="Mood-Based Recommender", layout="centered")
st.title("🎵 Mood-Based Product Recommendation")

if "selected_image" not in st.session_state:
    st.session_state.selected_image = None
if "selected_question" not in st.session_state:
    st.session_state.selected_question = None
if "selected_option" not in st.session_state:
    st.session_state.selected_option = None
if "show_question_popup" not in st.session_state:
    st.session_state.show_question_popup = False
if "show_recommendation_popup" not in st.session_state:
    st.session_state.show_recommendation_popup = False

# Show random images pop up
@st.dialog("Select an Image")
def image():
    st.write("Choose an image to continue:")

    selected_images = random.sample(list(image_question_map.keys()), 4)
    cols = st.columns(len(selected_images))

    for i, img in enumerate(selected_images):
        with cols[i]:
            st.image(img, caption=img, use_container_width=True)
            if st.button(f"Select image", key=img):
                st.session_state.selected_image = img
                st.session_state.show_question_popup = True
                st.rerun()

if st.session_state.selected_image is None:
    image()

# show question option pop up
@st.dialog("Answer this question")
def questions():
    img = st.session_state.selected_image
    question, options = random.choice(image_question_map[img])
    
    st.session_state.selected_question = question
    st.session_state.options = options
    st.subheader(question)
    selected_option = st.radio("Choose an option:", options, key='selected option')

    if st.button("Submit"):
        st.session_state.selected_option = selected_option
        st.session_state.show_question_popup = False
        st.session_state.show_recommendation_popup = True
        st.rerun()

if st.session_state.show_question_popup and st.session_state.selected_image:
    questions()


# Pop-up for Recommendation
@st.dialog("Your Final Recommendation")
def ask_recommendations():
    selected_option = st.session_state.selected_option
    selected_image = st.session_state.selected_image
    if selected_image not in recommendations_dict:
        st.error("No recommendations available for this choice.")
        return
    recommendations = []
    
    # Iterate through the dictionary and collect all matching recommendations
    for (category, item_type), items in recommendations_dict[f"{selected_image}"]['recommendations'].items():
        if selected_option in (category, item_type):  # Match category or item type
            recommendations.extend(items)
    
    # Remove duplicates and return
    recommendation = list(set(recommendations)) if recommendations else ["No recommendation available"]

    st.subheader("Based on your choices, we recommend:")
    st.write(recommendation)

    if st.button("🔄 Restart"):
        st.session_state.selected_image = None
        st.session_state.selected_question = None
        st.session_state.selected_option = None
        st.session_state.show_question_popup = False
        st.session_state.show_recommendation_popup = False
        st.rerun()

if st.session_state.show_recommendation_popup and st.session_state.selected_option:
    ask_recommendations()

    