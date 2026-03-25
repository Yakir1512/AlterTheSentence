

class LanguageConverter:
    """מחלקת עזר שמטפלת בכל הלוגיקה של זיהוי והמרת השפות"""
    
    def __init__(self):
        # הגדרת מפות ההמרה כמשתני מחלקה פנימיים
        eng_keys = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,.;'/"
        heb_keys = "/'קראטוןםפשדגכעיחלךזסבהנמצ/'קראטוןםפשדגכעיחלךזסבהנמצתץף,."
        
        self.eng_to_heb_map = str.maketrans(eng_keys, heb_keys)
        self.heb_to_eng_map = str.maketrans(heb_keys, eng_keys)

    def _get_char_language(self, char):
        """מתודה פרטית לזיהוי שפת התו"""
        if 'a' <= char.lower() <= 'z':
            return 'eng'
        elif 'א' <= char <= 'ת':
            return 'heb'
        return 'neutral'

    def convert(self, text):
        """המתודה הראשית שמקבלת טקסט מעורב ומחזירה טקסט מומר לפי גושים"""
        if not text:
            return ""
            
        result = ""
        current_chunk = ""
        current_lang = None 

        for char in text:
            char_lang = self._get_char_language(char)
            
            if char_lang == 'neutral':
                current_chunk += char
            elif current_lang is None:
                current_lang = char_lang
                current_chunk += char
            elif char_lang == current_lang:
                current_chunk += char
            else:
                # זיהינו החלפת שפה - ממירים את הגוש הקודם
                if current_lang == 'eng':
                    result += current_chunk.translate(self.eng_to_heb_map)
                else:
                    result += current_chunk.translate(self.heb_to_eng_map)
                
                # מאתחלים את הגוש החדש
                current_chunk = char
                current_lang = char_lang
                
        # טיפול בגוש האחרון שנשאר אחרי שהלולאה מסתיימת
        if current_chunk:
            if current_lang == 'eng':
                result += current_chunk.translate(self.eng_to_heb_map)
            elif current_lang == 'heb':
                result += current_chunk.translate(self.heb_to_eng_map)
            else: 
                result += current_chunk
                
        return result


