import os

def replace_in_file(fp):
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('Players:GetPlayers()', 'BS.GetPlayers()')
    content = content.replace('p.Character', 'BS.GetCharacter(p)')
    content = content.replace('player.Character', 'BS.GetCharacter(player)')
    content = content.replace('pd.player.Character', 'BS.GetCharacter(pd.player)')
    content = content.replace('lplr.Character', 'BS.GetCharacter(lplr)')
    content = content.replace('pChar', 'BS.GetCharacter(player)') # some use pChar = player.Character but the original has already been replaced? Wait, world.lua uses pChar.
    
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)

folder = r'C:\Users\pc\Videos\Radeon ReLive\TheOutlaw\YagmurStrike\modules'
for file in os.listdir(folder):
    if file.endswith('.lua'):
        replace_in_file(os.path.join(folder, file))

core_add = """
-- BLOXSTRIKE CUSTOM TARGET RESOLVERS
function BS.GetPlayers()
    local result = {}
    local Players = game:GetService("Players")
    for _, p in ipairs(Players:GetPlayers()) do
        table.insert(result, p)
    end
    -- Add mock players if they exist in Characters but not in Players (bots)
    local chars = workspace:FindFirstChild("Characters")
    if chars then
        for _, team in ipairs(chars:GetChildren()) do
            for _, c in ipairs(team:GetChildren()) do
                local isPlayer = false
                for _, p in ipairs(Players:GetPlayers()) do
                    if p.Name == c.Name then isPlayer = true; break end
                end
                if not isPlayer and c:IsA("Model") and c:FindFirstChild("Humanoid") then
                    table.insert(result, {
                        Name = c.Name,
                        DisplayName = c.Name,
                        UserId = 0,
                        Team = nil,
                        TeamColor = nil,
                        MockCharacter = c
                    })
                end
            end
        end
    end
    return result
end

function BS.GetCharacter(player)
    if not player then return nil end
    if type(player) == "table" and player.MockCharacter then return player.MockCharacter end
    
    -- Check workspace.Characters first
    local chars = workspace:FindFirstChild("Characters")
    if chars then
        for _, team in ipairs(chars:GetChildren()) do
            local c = team:FindFirstChild(player.Name)
            if c then return c end
        end
    end
    
    if typeof(player) == "Instance" and player:IsA("Player") then
        return player.Character
    end
    return nil
end
"""
with open(os.path.join(folder, 'core.lua'), 'a', encoding='utf-8') as f:
    f.write(core_add)
print('Done!')
