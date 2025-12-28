<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RS_RAYHAN VIP AUTO</title>
    <style>
        :root { --red: #ff003c; --cyan: #00f3ff; }
        body { background: #000; color: #fff; font-family: 'Courier New', monospace; text-align: center; margin: 0; display: flex; align-items: center; justify-content: center; height: 100vh; overflow: hidden; }
        .app-card { width: 90%; max-width: 400px; padding: 30px; border: 2px solid var(--red); border-radius: 20px; box-shadow: 0 0 30px var(--red); background: rgba(0,0,0,0.95); }
        .timer { font-size: 60px; font-weight: bold; color: var(--cyan); text-shadow: 0 0 15px var(--cyan); margin: 20px 0; }
        .period-box { font-size: 16px; background: rgba(255,0,60,0.1); padding: 12px; border-radius: 10px; border: 1px dashed var(--red); margin-bottom: 25px; }
        .prediction-box { width: 180px; height: 180px; border: 5px double var(--red); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto; transition: 0.5s; box-shadow: 0 0 15px var(--red); }
        #resultText { font-size: 35px; font-weight: bold; letter-spacing: 2px; }
        .voice-btn { margin-top: 15px; padding: 10px 20px; background: var(--red); color: white; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; }
    </style>
</head>
<body>

    <div class="app-card">
        <h2 style="color: var(--red); letter-spacing: 3px; margin: 0;">𝑹𝑺_𝑹𝑨𝒀𝑯𝑨𝑵 𝑽𝑰𝑷</h2>
        <div class="timer" id="timerDisplay">00:30</div>
        
        <div class="period-box">
            <span style="color: #aaa; font-size: 12px;">LIVE PERIOD</span><br>
            <span id="periodText" style="color: var(--cyan); font-weight: bold;">LOADING...</span>
        </div>

        <div class="prediction-box" id="displayBox">
            <div id="resultText">WAIT</div>
        </div>
        
        <p style="font-size: 11px; color: #555; margin-top: 20px;">AUTOMATED SIGNAL SYSTEM</p>
        <button class="voice-btn" onclick="activateVoice()">ENABLE VOICE 🔊</button>
    </div>

    <script>
        const BOT_TOKEN = '8564357681:AAHERKPgVWgxf9ecRKQrMqeIHmJnn6IBX0c'; 
        const CHAT_ID = '-1002396116905'; 
        let lastProcessedPeriod = "";
        let voiceEnabled = false;

        // ব্রাউজার ভয়েস পারমিশন অ্যাক্টিভেট করা
        function activateVoice() {
            voiceEnabled = true;
            const speech = new SpeechSynthesisUtterance("System Connected");
            window.speechSynthesis.speak(speech);
            document.querySelector('.voice-btn').style.display = 'none';
        }

        function updateClock() {
            const now = new Date();
            const y = now.getUTCFullYear();
            const m = String(now.getUTCMonth() + 1).padStart(2, '0');
            const d = String(now.getUTCDate()).padStart(2, '0');
            const dateStr = `${y}${m}${d}`;

            const secondsInDay = (now.getUTCHours() * 3600) + (now.getUTCMinutes() * 60) + now.getUTCSeconds();
            const slot = Math.floor(secondsInDay / 30) + 1; 
            const currentPeriod = `${dateStr}1000${String(slot).padStart(5, '0')}`;
            
            document.getElementById('periodText').innerText = currentPeriod;
            const remaining = 30 - (now.getUTCSeconds() % 30);
            document.getElementById('timerDisplay').innerText = `00:${remaining.toString().padStart(2, '0')}`;

            // নতুন পিরিয়ড শুরু হওয়ার ২-৩ সেকেন্ডের মাথায় সিগন্যাল
            if (remaining === 27 && currentPeriod !== lastProcessedPeriod) {
                generatePrediction(currentPeriod);
                lastProcessedPeriod = currentPeriod;
            }
        }

        function generatePrediction(period) {
            const isBig = Math.random() > 0.5;
            const num = isBig ? Math.floor(Math.random()*5)+5 : Math.floor(Math.random()*5);
            const result = isBig ? "BIG" : "SMALL";

            document.getElementById('resultText').innerText = result;
            document.getElementById('displayBox').style.borderColor = isBig ? "var(--red)" : "var(--cyan)";
            document.getElementById('displayBox').style.boxShadow = `0 0 25px ${isBig ? "var(--red)" : "var(--cyan)"}`;
            
            sendToTelegram(period, result, num);
            announceVoice(result);
        }

        function sendToTelegram(period, res, num) {
            const message = `🚀 *𝑹𝑺_𝑹𝑨𝒀𝑯𝑨𝑵 𝑽𝑰𝑷 𝑺𝑰𝑮𝑵𝑨𝑳* 🤖%0A` +
                            `━━━━━━━━━━━━━━━━━━━━%0A` +
                            `💎 *𝑴𝑨𝑹𝑲𝑬𝑻:* \`WINGO 30S\`%0A` +
                            `📅 *𝑷𝑬𝑹𝑰𝑶𝑫:* \`${period}\` %0A%0A` +
                            `🔮 *𝑷𝑹𝑬𝑫𝑰𝑪𝑻𝑰𝑶𝑵:* *${res} (${num})*%0A` +
                            `⚠️ *𝑨𝑫𝑽𝑰𝑪𝑬:* \`Use 7 Level Martingale\`%0A` +
                            `━━━━━━━━━━━━━━━━━━━━%0A` +
                            `🔥 *𝑺𝑻𝑨𝑻𝑼𝑺:* \`24/7 AUTO ONLINE\``;

            const url = `https://api.telegram.org/bot${BOT_TOKEN}/sendMessage?chat_id=${CHAT_ID}&text=${message}&parse_mode=Markdown`;
            fetch(url).catch(err => console.log("Telegram Error: ", err));
        }

        function announceVoice(res) {
            if (voiceEnabled && 'speechSynthesis' in window) {
                const speech = new SpeechSynthesisUtterance("Next result " + res);
                window.speechSynthesis.cancel();
                window.speechSynthesis.speak(speech);
            }
        }

        setInterval(updateClock, 1000);
        window.onload = updateClock;
    </script>
</body>
</html>