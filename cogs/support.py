import requests

class Support:

    def get_fontawesome_url(self, icon_string):
        print(icon_string)
        # parts = icon_string.split(':')
        
        # if len(parts) == 3 and parts[0] == "font-awesome-5":
        #     icon_name = parts[1]
        #     style = parts[2]
            
        #     if style not in ["solid", "regular", "brands"]:
        #         raise ValueError("Invalid icon style. Should be 'solid', 'regular', or 'brands'.")
            
        #     url = f"https://github.com/FortAwesome/Font-Awesome/raw/master/svgs/{style}/{icon_name}.svg"

        #     try:
        #         return requests.get(url).content
        #     except Exception as e:
        #         print(f"Thumbnail svg is not found, found - {e}")
        # else:
        #     raise ValueError("Invalid icon string format.")

