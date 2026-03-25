import keyboard
import pyperclip
import time
from  LanguageConverter    import LanguageConverter
# ==========================================
# לוגיקת המערכת (האזנה למקלדת ולוח הגזירים)
# ==========================================

# יצירת מופע של מחלקת העזר
converter = LanguageConverter()

def process_highlighted_text():
    keyboard.release('ctrl')
    keyboard.release('shift')
    keyboard.release('a')
    
    # השהיה מינימלית כדי לתת למערכת ההפעלה לעדכן את מצב המקלדת
    time.sleep(0.05)
    # 1. העתקת הטקסט המסומן
    keyboard.send('ctrl+c')
    time.sleep(0.1) # המתנה קלה כדי לוודא שההעתקה הושלמה
    
    selected_text = pyperclip.paste()
    
    if not selected_text:
        return

    # 2. שימוש במופע המחלקה להמרת הטקסט
    converted_text = converter.convert(selected_text)
    
    # אם שום דבר לא השתנה, אין טעם להמשיך
    if converted_text == selected_text:
        return
        
    # 3. הכנסת הטקסט המומר ללוח הגזירים
    pyperclip.copy(converted_text)
    time.sleep(0.1) # המתנה קלה לפני ההדבקה
    
    # 4. הדבקת הטקסט המומר על גבי הטקסט המסומן
    keyboard.send('ctrl+v')


# הגדרת קיצור הדרך
hotkey = 'ctrl+shift+a'
keyboard.add_hotkey(hotkey, process_highlighted_text)

print(f"התוכנית מוכנה ורצה ברקע! סמן טקסט ולחץ על {hotkey}. לחץ Esc כדי לסגור את התוכנית.")
keyboard.wait('esc')