# ==========================================
# File: features/main_logic.py
# Description: Steel AI - Smart Wardrobe & Weekly Planner Logic
# Core Features: Wardrobe Management, Weather-Aware Outfits, 
# Smart Alerts (Sunscreen/Umbrella), and Weekly Scheduling.
# ==========================================

import datetime
import random

class SteelAI_Engine:
    def __init__(self, user_name="Misafir"):
        self.user_name = user_name
        # Kullanıcının yüklediği dijital gardırop (Örnek veriler)
        self.wardrobe = {
            "ust_giyim": ["Beyaz Tişört", "Siyah Sweatshirt", "Keten Gömlek", "Yün Kazak", "Yağmurluk"],
            "alt_giyim": ["Mavi Jean", "Siyah Kumaş Pantolon", "Şort", "Eşofman Altı"],
            "dis_giyim": ["Kaşe Kaban", "Hafif Ceket", "Trençkot"],
            "ayakkabi": ["Spor Ayakkabı", "Bot", "Klasik Ayakkabı"]
        }
        
    def get_weather_forecast(self):
        """
        Haftalık hava durumu simülasyonu. 
        Gerçek uygulamada bir Hava Durumu API'sinden veri çeker.
        """
        forecast = [
            {"gun": "Pazartesi", "derece": 22, "durum": "Güneşli"},
            {"gun": "Salı", "derece": 12, "durum": "Yağmurlu"},
            {"gun": "Çarşamba", "derece": 18, "durum": "Parçalı Bulutlu"},
            {"gun": "Perşembe", "derece": 25, "durum": "Aşırı Güneşli"},
            {"gun": "Cuma", "derece": 10, "durum": "Soğuk/Rüzgarlı"}
        ]
        return forecast

    def generate_smart_alert(self, weather_condition):
        """
        Hava durumuna göre akıllı sağlık uyarıları oluşturur.
        """
        alerts = {
            "Güneşli": "☀️ Bugün hava çok parlak! Cildini korumak için Güneş Kremi sürmeyi unutma.",
            "Aşırı Güneşli": "🔥 UV indeksi yüksek! Şapkanı al ve güneş kremini tazelemeyi ihmal etme.",
            "Yağmurlu": "☔ Dikkat, yağış bekleniyor! Şemsiyeni mutlaka yanına al ve su geçirmeyen ayakkabılar seç.",
            "Soğuk/Rüzgarlı": "🌬️ Hava sertleşiyor. Boğazını korumak için bir atkı alabilirsin, hastalıklara dikkat!"
        }
        return alerts.get(weather_condition, "Bugün hava dengeli, keyfini çıkar!")

    def suggest_outfit(self, day_data):
        """
        Gardıroptaki kıyafetler ile hava durumunu eşleştiren AI mantığı.
        """
        temp = day_data["derece"]
        cond = day_data["durum"]
        
        outfit = []
        
        if temp > 20:
            outfit = [self.wardrobe["ust_giyim"][0], self.wardrobe["alt_giyim"][2], self.wardrobe["ayakkabi"][0]]
        elif 15 <= temp <= 20:
            outfit = [self.wardrobe["ust_giyim"][2], self.wardrobe["alt_giyim"][0], self.wardrobe["ayakkabi"][0]]
        else:
            outfit = [self.wardrobe["ust_giyim"][3], self.wardrobe["dis_giyim"][0], self.wardrobe["alt_giyim"][1], self.wardrobe["ayakkabi"][1]]
            
        return outfit

    def create_weekly_plan(self):
        """
        Kullanıcı için haftalık giyim programı oluşturur.
        """
        print(f"--- {self.user_name} İçin Haftalık Steel AI Planı ---\n")
        forecasts = self.get_weather_forecast()
        
        for day in forecasts:
            outfit = self.suggest_outfit(day)
            alert = self.generate_smart_alert(day["durum"])
            
            print(f"📅 {day['gun']} ({day['durum']} - {day['derece']}°C)")
            print(f"👕 Kombin: {', '.join(outfit)}")
            print(f"💡 AI Notu: {alert}")
            print("-" * 30)

# --- Uygulamayı Çalıştır (Demo Modu) ---
if __name__ == "__main__":
    app = SteelAI_Engine(user_name="Özge")
    app.create_weekly_plan()
