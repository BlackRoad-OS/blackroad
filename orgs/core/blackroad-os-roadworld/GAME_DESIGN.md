# RoadWorld: Open World Game Design

## Game Concept

**RoadWorld** transforms the entire planet into an open-world exploration game where players explore real-world locations, complete missions, collect items, and compete with others.

## Core Game Loop

```
Explore Real World → Discover Locations → Complete Missions → Earn Rewards
       ↓                    ↓                     ↓                ↓
   Move Avatar      Find Collectibles      Gain XP/Points    Unlock Abilities
       ↓                    ↓                     ↓                ↓
   Level Up         Build Collection        Complete Quests   Compete on Leaderboards
       ↑_____________________________________________________________↓
                        Continue Exploring
```

## Game Features

### 1. Player Avatar System
- **Avatar**: Animated player character on the map
- **Movement**: Click-to-move or WASD controls
- **Speed**: Walking, running, vehicle modes
- **Position**: GPS-based real location
- **Visibility**: See yourself and nearby players
- **Customization**: Avatar skins, colors, accessories

### 2. Discovery & Exploration
- **Landmarks**: Real-world POIs to discover
- **Hidden Locations**: Secret spots to find
- **Territory**: Claim areas by visiting
- **Fog of War**: Reveal map by exploring
- **Travel Log**: Track places visited
- **Distance Traveled**: Cumulative stats

### 3. Collectibles System
- **Types**:
  - 🌟 Stars: Common collectibles
  - 💎 Gems: Rare finds
  - 🏆 Trophies: Achievement rewards
  - 🎁 Mystery Boxes: Random loot
  - 📜 Artifacts: Historical items
  - 🗝️ Keys: Unlock special areas

- **Placement**: Auto-generated near landmarks
- **Rarity**: Common, Uncommon, Rare, Epic, Legendary
- **Collection**: Auto-collect when near
- **Storage**: Unlimited inventory

### 4. Mission System
- **Daily Missions**:
  - Visit specific location type
  - Travel X kilometers
  - Collect Y items
  - Complete in Z time

- **Story Missions**:
  - Multi-step quests
  - Narrative-driven
  - Unlock new areas
  - Major rewards

- **Challenges**:
  - Timed objectives
  - Competitive events
  - Global participation
  - Limited-time rewards

### 5. Progression System
- **XP Sources**:
  - Discovering new locations: 100 XP
  - Collecting items: 10-500 XP
  - Completing missions: 500-5000 XP
  - Daily login: 50 XP
  - Social actions: 25 XP

- **Levels**: 1-100
- **Prestige**: Reset to level 1 with bonuses
- **Abilities**: Unlock as you level
  - Level 5: Fast Travel
  - Level 10: Vehicle Mode
  - Level 20: Radar (see nearby items)
  - Level 30: Territory Claiming
  - Level 50: Teleport
  - Level 75: Flight Mode

### 6. Multiplayer Features
- **Real-time Presence**: See nearby players (100m radius)
- **Player Profiles**: View stats, achievements
- **Friend System**: Add friends, see their location
- **Teams/Guilds**: Create or join groups
- **Trading**: Exchange collectibles
- **Challenges**: Compete directly
- **Chat**: Location-based or global

### 7. Territory & Ownership
- **Claim Areas**: Visit to claim territory
- **Control Points**: Special locations to control
- **Team Territory**: Guild-based land ownership
- **Bonuses**: XP multipliers in your territory
- **Defense**: Protect from other players/teams
- **Revenue**: Earn passive points

### 8. Economy System
- **Currencies**:
  - 🪙 Coins: Earned through play
  - 💠 Gems: Premium currency
  - 🎖️ Tokens: Event currency

- **Shop**:
  - Avatar customization
  - Boosters (2x XP, speed)
  - Special items
  - Map themes

- **Earning**:
  - Complete missions
  - Sell collectibles
  - Daily rewards
  - Achievements

### 9. Achievements & Badges
- **Explorer Badges**:
  - Visit all continents
  - Discover 100 landmarks
  - Travel 1000km
  - Reach highest point

- **Collector Badges**:
  - Collect 1000 items
  - Complete all sets
  - Find all legendaries

- **Social Badges**:
  - Make 10 friends
  - Trade 100 items
  - Join a guild

- **Master Badges**:
  - Reach level 100
  - Complete all missions
  - Top 100 leaderboard

### 10. Leaderboards
- **Global Rankings**:
  - Total XP
  - Distance traveled
  - Items collected
  - Missions completed
  - Territory owned

- **Regional Rankings**: By continent/country/city
- **Friend Rankings**: Compare with friends
- **Guild Rankings**: Team competition
- **Weekly/Monthly**: Reset rankings

### 11. Events & Seasons
- **Daily Events**: Special spawns, bonus XP
- **Weekly Events**: Themed challenges
- **Seasonal Events**: Major updates
  - Spring: Nature theme
  - Summer: Beach theme
  - Fall: Harvest theme
  - Winter: Snow theme

- **Special Events**:
  - Treasure hunts
  - Race events
  - Building events
  - Community goals

### 12. Social Features
- **Player Profiles**:
  - Avatar display
  - Stats showcase
  - Achievement gallery
  - Collection display

- **Activities Feed**:
  - Recent discoveries
  - Mission completions
  - Rare finds
  - Level ups

- **Sharing**:
  - Screenshot locations
  - Share achievements
  - Invite friends
  - Post discoveries

## Art Direction

### Visual Style
- **Medium**: Hand-crafted pixel art (NOT emoji-derived)
- **Aesthetic**: Detailed, warm, richly textured -- inspired by Stardew Valley and Habbo Hotel
- **Palette**: Blues and warm wood tones as anchors; orange/yellow accents for BlackRoad branding
- **Rendering**: Clean outlines, subtle dithering for texture (wood grain, fabric), soft drop shadows

### Character Sprites
- **Proportions**: Chibi (large head, small body)
- **Resolution**: High-detail pixel art, legible at small scales
- **Hair**: Vibrant gradient coloring (red-orange-purple-blue spectrum)
- **Outfit**: Dark clothing with BlackRoad "B" logo, colorful accents
- **Accessories**: Headphones, branded gear
- **Animation**: Walk cycle frames, idle, interact
- **Background**: Transparent (composited onto environments)

### Furniture & Props
- **View**: Front-facing for individual items (couch, chair, desk)
- **Style**: Clean outlines, interior shading/highlights, subtle shadow beneath
- **Materials**: Realistic texturing -- wood grain on desks/tables, fabric dithering on upholstery
- **Color Consistency**: Blue upholstery, warm brown wood across all furniture sets
- **Categories**:
  - **Office**: Desk with drawers, office chair, conference table with chairs
  - **Residential**: Couch, bed, bookshelf, TV stand, dining table
  - **Appliances**: Fridge, stove, washer/dryer, microwave
  - **Recreation**: Pool table, foosball table, ping pong table, arcade machines, dartboard
  - **Commercial**: Vending machines, food counter, display cases, shelving

### Environment Views

#### Top-Down (Overworld / Building Layout)
- **Perspective**: Bird's-eye view, tile-based grid
- **Buildings**: Visible colored rooftops (yellow/brick, blue, slate gray)
- **Walls**: White/light gray brick exterior
- **Walkways**: Gray stone tile forming corridors and streets
- **Doors**: Brown wooden doors with doorknobs, "Welcome" mats at entrances
- **Outdoor**: Green grass areas, bushes, landscaping at borders
- **Purpose**: Overworld navigation, building selection, entering rooms

#### Side-View Cross-Section (Interiors)
- **Perspective**: 2D side-view cutaway showing room interiors
- **Rooms stacked vertically**: Multi-floor buildings displayed as cross-sections
- **Wall separators**: Visible between rooms, with floor/ceiling lines
- **Fully furnished**: Every room densely detailed with props, wall art, plants, lamps
- **Ambient details**: Pictures on walls, potted plants, rugs, lighting fixtures

### Location Types

#### Residential Interiors
- **Bedroom**: Bed, desk, computer, chair, bookshelf, wall art, lamps, rug
- **Bathroom**: Shower/tub, toilet, sink, vanity, cabinets
- **Living Room**: TV/entertainment center, couch, coffee table, bookshelves, wall art
- **Kitchen**: Stove, fridge, microwave, cabinets, dining table with chairs
- **Game Room**: Couch, dartboard, pool/foosball table, arcade machine, bookshelves
- **Laundry Room**: Washer, dryer, shelving, storage boxes
- **Media Room**: Large TV/screen, couch, ambient wall art, mood lighting
- **Lounge**: Couch with pillows, bookshelves, coffee table, utility equipment

#### BlackRoad HQ / Office
- **Branding**: "BLACKROAD" signage on walls and counters, branded color scheme
- **Color Variants**: Dark theme with orange accents (branded) / Blue-yellow theme (cafeteria)
- **Cafeteria**: Food counter with staff NPC, bar stools, menu displays
- **Dining Area**: Tables with chairs in rows, booth seating along windows
- **Break Room**: Vending machines, large TV/screens, plants, coffee station
- **Game Zone**: Pool table, foosball table, ping pong table, arcade cabinets
- **Screens**: Branded displays ("OrangeScreen", "RangeCrush" etc.)

#### Shopping Mall
- **Layout**: Multi-floor with central glass elevator, palm tree decorations
- **Store Types**:
  - **Tech Store**: Electronics displays, computer setups, demo stations
  - **Toyland**: Colorful toy displays, plush items, games
  - **Beauty**: Cosmetics counters, product shelves, pink/warm accents
  - **Fashion**: Clothing racks, mannequins, fitting area
  - **Sports**: Equipment displays, athletic gear, branded sections
  - **Arcade**: Cabinet machines, prize counters, neon accents
  - **Supermarket**: Aisles with produce, deli counter, refrigerated sections
- **Common Areas**: Food court with tables, walkways between stores
- **Signage**: Each store has a distinct colored sign above its entrance

### Asset Pipeline Requirements
- **Format**: PNG with transparency for sprites/props; full scene PNGs for environments
- **Loading**: Direct image texture loading (replaces emoji-to-Canvas pipeline)
- **Storage**: Cloudflare R2 for production assets
- **Sprite Sheets**: Group related animations (character walk cycles) into sheets
- **Tilesets**: Modular wall/floor/roof tiles for procedural room generation
- **LOD**: Full-detail assets for interior views; simplified versions for overworld zoom levels

## Technical Implementation

### Data Structure

```javascript
{
  player: {
    id: String,
    username: String,
    avatar: Object,
    position: [lng, lat],
    level: Number,
    xp: Number,
    stats: {
      distanceTraveled: Number,
      locationsDiscovered: Number,
      itemsCollected: Number,
      missionsCompleted: Number
    },
    inventory: Array,
    achievements: Array,
    territory: Array
  },

  gameWorld: {
    collectibles: Array,
    landmarks: Array,
    missions: Array,
    events: Array,
    players: Map
  }
}
```

### Architecture

```
Client (Browser)
    ↓
Game Engine (JS)
    ↓
    ├─ Player Manager
    ├─ World Manager
    ├─ Mission Manager
    ├─ Inventory Manager
    └─ Multiplayer Manager
    ↓
MapLibre GL (Rendering)
    ↓
Cloudflare Workers (Backend)
    ↓
    ├─ D1 Database (persistent data)
    ├─ KV Storage (real-time state)
    ├─ Durable Objects (multiplayer sync)
    └─ R2 Storage (assets)
```

## Game Modes

### 1. Free Roam
- Explore at your own pace
- No objectives
- Discover naturally
- Peaceful exploration

### 2. Mission Mode
- Objective-focused
- Time limits
- Rewards
- Progression

### 3. Competitive Mode
- PvP challenges
- Territory wars
- Racing
- Leaderboard climbing

### 4. Creative Mode
- Place custom markers
- Create missions
- Design routes
- Share with community

## Monetization (Optional)

### Free Features
- Core gameplay
- Basic avatar
- Standard missions
- Friend system
- Leaderboards

### Premium Features (Optional)
- Custom avatars
- Exclusive items
- 2x XP boost
- Priority events
- Ad-free
- Cloud save

## Balance & Fairness

- **No Pay-to-Win**: Premium only cosmetic/convenience
- **Regional Balance**: Adjust spawn rates by population
- **Rural Bonus**: Extra items in low-population areas
- **Fair Competition**: Separate leaderboards by region
- **Anti-Cheat**: Location verification, rate limiting

## Future Expansions

### Phase 1 (v3.0): Core Game
- Player avatar & movement
- Collectibles system
- Basic missions
- XP & levels
- Leaderboards

### Phase 2 (v3.5): Multiplayer
- Real-time player presence
- Friend system
- Trading
- Teams/guilds
- Chat

### Phase 3 (v4.0): Advanced Features
- Territory system
- Advanced missions
- Events & seasons
- Economy
- Achievements

### Phase 4 (v4.5+): Expansion
- AR integration
- Voice chat
- User-generated content
- Cross-platform sync
- Mobile apps

## Success Metrics

- Daily Active Users (DAU)
- Average session time
- Locations discovered
- Items collected
- Missions completed
- Player retention (D1, D7, D30)
- Social interactions
- Premium conversion

## Inspiration

- Pokémon GO: Location-based gameplay
- GeoGuessr: Real-world exploration
- Ingress: Territory control
- Geocaching: Hidden item discovery
- Flight Simulator: Real-world map
- Minecraft: Creative freedom

## Unique Selling Points

1. **Entire planet is playable** - Not just cities
2. **Real-world integration** - Actual landmarks
3. **No device required** - Web-based
4. **Cross-platform** - Desktop + mobile
5. **Educational** - Learn geography
6. **Social** - Connect with travelers
7. **Free to play** - No barriers

---

**RoadWorld: Explore the World, One Location at a Time** 🌍🎮
