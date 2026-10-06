-- YagmurStrike Launcher - loads via http_request (your executor game:HttpGet returns nil)
if game.PlaceId ~= 114234929420007 then warn("[BS] Wrong game!") return end
local u = "https://raw.githubusercontent.com/Yagmur1337/YagmurStrike/main/YagmurStrike_Standalone.lua?t=" .. tostring(math.floor(tick()*1000))
print("[BS] Launcher v4.1: downloading main script...")
local b = nil
if http_request then local ok,r = pcall(function() return http_request({Url=u,Method="GET"}) end) if ok and r and r.Body then b=r.Body end end
if not b and request then local ok,r = pcall(function() return request({Url=u,Method="GET"}) end) if ok and r and r.Body then b=r.Body end end
if not b and syn and syn.request then local ok,r = pcall(function() return syn.request({Url=u,Method="GET"}) end) if ok and r and r.Body then b=r.Body end end
if b and #b>100 then
    print("[BS] Got " .. #b .. " bytes, executing...")
    local fn,err = loadstring(b)
    if fn then fn() else warn("[BS] COMPILE: " .. tostring(err)) end
else
    warn("[BS] FAILED! All HTTP methods returned nil")
    warn("[BS] Copy YagmurStrike_Standalone.lua content directly into executor")
end
