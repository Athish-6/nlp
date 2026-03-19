tamil_dict = {
 "நாய்": "விலங்கு",
 "மரம்": "தாவரம்",
 "ஆசிரியர்": "தொழில்",
 "பழம்": "உணவு"
}
word = input("தமிழ் சொல் உள்ளிடவும்: ")
if word in tamil_dict:
 print("பொருள்:", tamil_dict[word])
else:
 print("சொல் அகராதியில் இல்லை")