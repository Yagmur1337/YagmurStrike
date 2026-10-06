import os, re

# All remaining Chinese strings found in the scan
TRANSLATIONS = {
    # cheatdetect.lua
    "關於": "About",
    "作弊偵測": "Cheat Detection",
    "自動掃描": "Auto Scan",
    "最低信心度": "Min Confidence",
    "顯示警告": "Show Alerts",
    "音效警告": "Sound Alert",
    "持續橫幅": "Persistent Banner",
    "可疑玩家標記": "Suspect Marker",
    "警告閾值": "Alert Threshold",
    "警示閾值": "Warn Threshold",
    "嚴重閾值": "Critical Threshold",
    "後座偵測": "RCS Detection",
    "第三人稱偵測": "Third Person Detection",

    # combat.lua
    "子彈穿牆": "Wallbang",
    "穿牆深度": "Wallbang Penetration",
    "自動偵測牆壁厚度": "Auto Detect Wall Thickness",
    "胸部": "Chest",
    "最近": "Nearest",
    "骨盆": "Pelvis",
    "腹部": "Stomach",
    "十字準星": "Crosshair",
    "淡出": "Fade Out",
    "貝塞爾": "Bezier",
    "自瞄平滑風格": "Aim Smooth Style",
    "自瞄穿牆檢查": "Aimbot Wall Check",
    "自瞄延遲刻度": "Aim Lag Ticks",
    "左Alt": "Left Alt",
    "左Ctrl": "Left Ctrl",
    "滑鼠4": "Mouse4",
    "滑鼠5": "Mouse5",
    "自瞄人性化": "Humanize Aimbot",
    "自瞄自動蹲": "Aimbot Auto Crouch",
    "自瞄目標線": "Aimbot Target Line",
    "靜默自瞄": "Silent Aimbot",
    "自瞄血量優先": "Aimbot Health Priority",
    "自瞄擊退": "Aimbot Knockback",
    "自瞄按鍵觸發": "Aimbot Key Trigger",
    "觸發器僅身體": "Triggerbot Body Only",
    "觸發器正常隨機": "Triggerbot Legit Random",
    "靜默瞄準": "Silent Aim",
    "自動射擊": "Auto Fire",
    "無散布": "No Spread",
    "好友檢查": "Friend Check",
    "瞄準輔助": "Aim Assist",
    "反瞄視野": "Anti-Aim FOV",
    "自動刀人": "Auto Knife",
    "購買主武器": "Buy Primary",
    "購買副武器": "Buy Secondary",
    "強制準星": "Force Crosshair",
    "開鏡縮放調整": "Scope Zoom Adjust",
    "快速射擊": "Rapid Fire",
    "快速自動急停": "Rapid Auto Stop",
    "最低傷害過濾": "Min Damage Filter",
    "覆蓋爆頭最低傷害": "Override HS Min Damage",
    "空彈自動換彈": "Auto Reload on Empty",
    "啟用延遲補償": "Enable Lag Comp",
    "友軍火力": "Friendly Fire",

    # combatassist.lua
    "自動回覆": "Auto Reply",
    "擊殺自動嘲諷": "Auto Kill Taunt",
    "自動 GG": "Auto GG",
    "自動隊友報位": "Auto Callout",
    "觀戰歷史": "Spectator History",
    "自動套用設定": "Auto Apply Settings",
    "記錄表現": "Record Performance",
    "場次統計": "Session Stats",
    "重置場次統計": "Reset Session Stats",

    # esp.lua
    "方框透視": "Box ESP",
    "血量文字": "Health Text",
    "血量位置": "Health Position",
    "距離單位": "Distance Unit",
    "追蹤線": "Tracer",
    "骨骼透視": "Skeleton ESP",
    "離屏箭頭": "Off-Screen Arrow",
    "速度箭頭": "Velocity Arrow",
    "目標透視": "Target ESP",
    "雷射線": "Laser Line",
    "方框風格": "Box Style",
    "自定義": "Custom",
    "透視輪廓": "ESP Outline",
    "彩虹透視速度": "Rainbow ESP Speed",
    "浮水印": "Watermark",
    "狀態顯示": "Status Display",
    "雷達透視": "Radar ESP",
    "雷達背景": "Radar Background",
    "指南針": "Compass",
    "距離限制": "Distance Limit",
    "按距離排序": "Sort By Distance",
    "視野圈大小": "FOV Circle Size",
    "視野填充": "FOV Fill",
    "十字準星": "Crosshair",
    "十字準星粗細": "Crosshair Thickness",
    "十字準星點": "Crosshair Dot",
    "十字準星風格": "Crosshair Style",
    "十字準星輪廓": "Crosshair Outline",
    "第三人稱自動縮放": "Third Person Auto Zoom",
    "第三人稱平滑": "Third Person Smooth",
    "第三人稱頭部追蹤": "Third Person Head Track",
    "角色角度": "Viewmodel Angle",
    "角色縮放": "Viewmodel Scale",
    "角色視野": "Viewmodel FOV",
    "游擊": "Guerrilla",
    "預設": "Default",
    "聲音透視": "Sound ESP",
    "預測線": "Prediction Line",

    # hud.lua
    "記憶體顯示": "Memory Display",
    "伺服器資訊": "Server Info",
    "已啟用模組": "Active Modules",
    "武器資訊": "Weapon Info",
    "玩家資訊": "Player Info",
    "戰鬥 HUD": "Combat HUD",
    "浮水印": "Watermark",
    "CS2 風格": "CS2 Style",
    "預設": "Default",
    "顯示延遲": "Show Ping",
    "顯示伺服器": "Show Server",
    "觀戰通知": "Spectate Notification",
    "顯示命中率": "Show Hit Rate",

    # killeffects.lua
    "命中標記風格": "Hitmarker Style",
    "CS2 風格": "CS2 Style",
    "爆頭標記": "Headshot Marker",
    "金屬管": "Metal Pipe",
    "命中音效音量": "Hit Sound Volume",
    "慢動作": "Slow Motion",
    "擊殺音效音量": "Kill Sound Volume",

    # pingadapt.lua
    "適應模式": "Adapt Mode",
    "平衡": "Balanced",
    "延遲自動恐慌": "Ping Auto Panic",
    "自動延遲補償": "Auto Lag Comp",
    "自動視野": "Auto FOV",
    "自動假延遲": "Auto Fake Lag",

    # rage.lua
    "牆壁穿透": "Wall Penetration",
    "解析模式": "Resolver Mode",
    "刀殺": "Knife Kill",
    "自動反制": "Auto Resolve",

    # smartai.lua
    "距离": "Distance",
    "综合": "Composite",
    "移动模式识别": "Movement Pattern Recognition",

    # stealth.lua
    "清除呼叫堆疊": "Clear Call Stack",
    "從 getgenv 隱藏": "Hide From getgenv",
    "清除環境": "Clean Environment",
    "偽造 checkcaller": "Spoof checkcaller",
    "隱藏 CoreGui": "Hide CoreGui",
    "對玩家隱藏": "Hide From Players",
    "風險計算器": "Risk Calculator",
    "靜默模式": "Silent Mode",
    "反重播": "Anti Replay",
    "封包混淆": "Packet Obfuscation",
    "記憶體清理": "Memory Cleanup",
    "反調試": "Anti Debug",
    "伺服器驗證繞過": "Server Validation Bypass",
    "緊急斷線": "Emergency Disconnect",
    "自動踢出偵測": "Auto Kick Detection",
    "行為隨機化": "Behavior Randomization",
    "全限速": "Global Rate Limit",
    "白名單管理員": "Whitelist Admin",
    "風險時換服": "Server Hop On Risk",
    "HVH 安全模式": "HVH Safe Mode",
    "反信任分數繞過": "Anti Trust Score Bypass",
    "行為一致性": "Behavior Consistency",
    "擊殺模式偽裝": "Kill Pattern Mask",
    "移動正常性": "Legit Movement",
    "瞄準正常性": "Legit Aim",
    "反統計偵測": "Anti Stat Detection",
    "伺服器驗證偽裝": "Server Validation Mask",
    "場次暖身": "Session Warmup",
    "逐步升級": "Gradual Escalation",
    "反統計尖峰": "Anti Stat Spike",
    "擊殺冷卻": "Kill Cooldown",
    "假失彈": "Fake Miss",
    "瞄準延遲變化": "Aim Delay Variation",
    "移動模式": "Move Pattern",
    "十字準星靜止": "Crosshair Idle",
    "環顧": "Look Around",
    "KD 平衡": "KD Balance",
    "爆頭率限制": "HS Rate Limit",
    "傷害分佈": "Damage Distribution",
    "風險時恐慌": "Panic On Risk",
    "被封時換服": "Server Hop On Ban",
    "自動帳號切換": "Auto Account Switch",
    "速度上限": "Velocity Cap",
    "位置漂移": "Position Drift",
    "延遲模擬": "Ping Simulation",
    "呼叫堆疊與調試": "Call Stack & Debug",
    "環境隱藏": "Environment Hide",
    "鉤子偽裝": "Hook Masking",
    "字串混淆": "String Obfuscation",
    "動作模糊": "Action Fuzz",
    "模糊量": "Fuzz Amount",
    "序列隨機化": "Sequence Randomize",
    "時序不同步": "Timing Desync",
    "時序隨機化": "Timing Randomize",
    "記憶體規避": "Memory Evasion",
    "字串加密": "String Encryption",
    "物件混亂": "Object Scramble",
    "引用清理": "Reference Cleanup",
    "GC混淆": "GC Obfuscation",
    "反模擬": "Anti Emulation",
    "沙箱偵測": "Sandbox Detection",
    "時序預警": "Timing Canary",
    "環境完整性": "Env Integrity",
    "自我治療": "Self Heal",
    "反截圖": "Anti Screenshot",

    # world.lua
    "開鏡視野": "ADS FOV",
    "煙霧透視": "Smoke Reveal",
    "手榴彈軌跡": "Grenade Trajectory",
    "夜視模式": "Night Vision",
    "自定義十字準星顏色": "Custom Crosshair Color",
    "移除煙霧": "Remove Smoke",

    # utility.lua
    "長跳": "Long Jump",
    "連跳加強": "Bhop Boost",
    "邊緣蟲": "Edgebug",
    "Stamina": "Stamina",
    "地面模式": "Ground Mode",
    "跳投": "Jump Throw",
    "快速投擲": "Quick Throw",

    # ui.lua
    "夜視模式": "Night Vision",

    # Standalone module names
    "反檢測": "Anti-Cheat Bypass",
    "作弊偵測": "Cheat Detection",
    "戰鬥系統": "Combat System",
    "戰鬥輔助": "Combat Assist",
    "兼容層": "Compat Layer",
    "核心": "Core",
    "錯誤處理": "Error Handler",
    "透視系統": "ESP System",
    "事件系統": "Event System",
    "HUD顯示": "HUD Display",
    "Luau兼容": "Luau Compat",
    "Luau偵測": "Luau Detect",
    "暴力系統": "Rage System",
    "智能AI": "Smart AI",
    "隱身系統": "Stealth System",
    "介面": "Interface",
    "工具": "Utility",
    "視角模型": "Viewmodel",
    "普通": "Normal",

    # Labels in stealth
    " ML  ": " ML  ",
}

dir_path = r'C:\Users\pc\Videos\Radeon ReLive\TheOutlaw\YagmurStrike'
sorted_translations = sorted(TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True)

updated = 0
for root, dirs, files in os.walk(dir_path):
    dirs[:] = [d for d in dirs if d != '.git']
    for file in files:
        if not file.endswith('.lua'):
            continue
        fp = os.path.join(root, file)
        with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        original = content
        for zh, en in sorted_translations:
            if zh in content:
                # Replace in any context (quoted strings, comments, etc.)
                content = content.replace(zh, en)
        if content != original:
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(content)
            updated += 1
            print(f"Updated: {file}")

print(f"\nDone. {updated} files updated.")
