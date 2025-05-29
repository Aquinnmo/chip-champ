# Chip Champ Detailed Development Plan

## Project Overview

**Chip Champ** is a web-based Texas Hold 'Em poker chip management service that eliminates the need for physical chips in in-person games. Players use their individual devices to manage betting, while cards are dealt physically. The service handles all chip tracking, side pots, blind rotation, and win distribution automatically.

### Core Features
- Multi-player game lobbies with unique join codes
- Real-time chip stack and pot tracking
- Automatic blind and dealer rotation
- Individual device betting interface optimized for mobile (fold, call, raise, all-in)
- Side pot calculation for all-in scenarios
- Player elimination and cash-out tracking
- Real-time game state synchronization across all devices

## Technical Architecture

### Tech Stack
- **Frontend**: React 18 with TypeScript, bootstrap for styling
- **Backend**: Node.js with Express.js and TypeScript
- **Database**: Redis (game state) + MongoDB (persistence)
- **Real-time**: Socket.IO for WebSocket communication
- **Build Tools**: Vite for frontend, nodemon for backend development

### Backend Structure (Node.js + Express)
TypeScript Node.js service made from scratch, using `/noble_terminal` as a loose guideline:

#### Core Services
- **GameService**: Manages game state, rounds, pot, blinds (example being `objects.py`)
- **PlayerService**: Handles individual player chip stacks and actions
- **BettingService**: Call, raise, fold, all-in logic validation
- **SidePotService**: Handle multiple all-in scenarios and pot splitting
- **RedisService**: Real-time game state storage and retrieval
- **MongoService**: Persistent game history and player data

#### Express.js Components
- **Routes**: RESTful API endpoints for game operations
- **Middleware**: Authentication, validation, error handling
- **Socket.IO**: Real-time WebSocket event handlers
- **Controllers**: Business logic layer between routes and services

### Frontend Structure (React + TypeScript)
- **Components**: Reusable UI elements (PlayerCard, ChipStack, BettingControls)
- **Pages**: Lobby, Game, Results screens
- **Hooks**: Custom hooks for Socket.IO, game state management
- **Context**: React Context for global state (user session, current game)
- **Services**: API calls and Socket.IO client management

### Data Flow Architecture
1. **Redis**: Active game state, player sessions, real-time updates
2. **Socket.IO**: Bi-directional real-time communication
3. **MongoDB**: Game history, player statistics, completed games
4. **React State**: Local UI state with Socket.IO synchronization

## Throughout Development

**DURING THE ENTIRE DEVELOPMENT PROCESS** you will test any changes with rigourous unittesting. unittests will be added vigourously.

## Development Phases

### Phase 1: Backend Infrastructure & Core API (Week 1-2)
**Goal**: Set up Node.js/Express backend with Redis/MongoDB and port existing game logic

#### 1.1 Project Setup & Dependencies
```bash
npm init -y
npm install express typescript ts-node @types/node @types/express
npm install socket.io redis@^4.0.0 mongodb mongoose
npm install cors helmet express-rate-limit
npm install -D nodemon @types/mongoose
```

**Note**: Redis v4+ includes TypeScript definitions, no need for @types/redis

#### 1.2 TypeScript Configuration
- Configure `tsconfig.json` for Node.js
- Set up development scripts with nodemon
- Configure ES modules and strict type checking

#### 1.3 Game Logic Migration (from Python to TypeScript)
- **GameService.ts**: Port `Game` class from `objects.py`
  - Betting round management
  - Pot calculation logic
  - Dealer/blind rotation
  - Player turn management
- **PlayerService.ts**: Port `Player` class functionality
  - Chip stack management
  - Betting actions validation
  - Player status tracking
- **SidePotService.ts**: Implement side pot splitting algorithms

#### 1.4 Database Setup
- **Redis Configuration**: 
  - Game state storage with TTL
  - Player session management
  - Pub/Sub for real-time updates
- **MongoDB Configuration**:
  - Game history schema
  - Player statistics
  - Connection pooling

#### 1.5 Express API Routes
```typescript
// Game management routes
POST   /api/games              // Create new game
GET    /api/games/:gameId      // Get game state
POST   /api/games/:gameId/join // Join game
DELETE /api/games/:gameId/leave // Leave game

// Game actions
POST   /api/games/:gameId/start    // Start game
POST   /api/games/:gameId/action   // Submit betting action
POST   /api/games/:gameId/winner   // Declare winner
POST   /api/games/:gameId/next     // Next hand
```

#### 1.6 Testing Framework
- Jest configuration for TypeScript
- Unit tests for game logic services
- API endpoint testing with supertest
- Redis/MongoDB mocking for tests

### Phase 2: Real-time WebSocket Implementation (Week 2-3)
**Goal**: Implement Socket.IO for real-time game synchronization

#### 2.1 Socket.IO Server Setup
```typescript
// Socket event handlers
'join-game'     // Player joins game room
'leave-game'    // Player leaves game
'betting-action' // Place bet, call, fold, raise
'game-update'   // Broadcast game state changes
'player-update' // Individual player updates
'error'         // Error handling and validation
```

#### 2.2 Real-time Event Architecture
- **Room Management**: Socket.IO rooms for game isolation
- **Event Broadcasting**: Selective updates to specific players
- **State Synchronization**: Redis pub/sub integration (optional for single-server deployment)
- **Connection Recovery**: Rejoin game on reconnection

#### 2.3 Game State Broadcasting
- **Full State Updates**: New players joining, game start/end
- **Incremental Updates**: Betting actions, pot changes
- **Player-specific Updates**: Private information (hole cards)
- **Optimistic Updates**: Immediate UI feedback with validation

#### 2.4 Error Handling & Validation
- **Server-side Validation**: All betting actions verified
- **Rate Limiting**: Prevent spam betting actions
- **Authentication**: Session-based player verification
- **Graceful Degradation**: Fallback to polling if WebSocket fails (optional for MVP - can be deferred)

### Phase 3: React Frontend Development (Week 3-4)
**Goal**: Build responsive React interface with real-time updates

#### 3.1 React Project Setup
```bash
npm create vite@latest chip-champ-frontend -- --template react-ts
cd chip-champ-frontend
npm install socket.io-client axios react-router-dom
npm install @types/socket.io-client
npm install tailwindcss @tailwindcss/forms
```

#### 3.2 Project Structure
```
src/
├── components/
│   ├── Game/
│   │   ├── BettingControls.tsx
│   │   ├── PlayerCard.tsx
│   │   ├── GameTable.tsx
│   │   └── ChipStack.tsx
│   ├── Lobby/
│   │   ├── CreateGame.tsx
│   │   ├── JoinGame.tsx
│   │   └── PlayerList.tsx
│   └── Common/
│       ├── LoadingSpinner.tsx
│       └── ErrorBoundary.tsx
├── hooks/
│   ├── useSocket.ts
│   ├── useGameState.ts
│   └── useLocalStorage.ts
├── services/
│   ├── api.ts
│   ├── socket.ts
│   └── gameService.ts
├── types/
│   ├── Game.ts
│   ├── Player.ts
│   └── API.ts
└── context/
    ├── GameContext.tsx
    └── SocketContext.tsx
```

#### 3.3 Core Components Development

**BettingControls.tsx**
```typescript
interface BettingControlsProps {
  currentPlayer: Player;
  gameState: GameState;
  onAction: (action: BettingAction) => void;
  disabled: boolean;
}
```

**GameTable.tsx**
- Display pot amount and betting round
- Show current player indicator
- Display community cards area (placeholder - for visual reference only)
- Responsive grid layout for players

**PlayerCard.tsx**
- Player name and chip stack
- Betting status (folded, all-in, active)
- Current bet amount
- Dealer/blind indicators

#### 3.4 Socket.IO Integration
```typescript
// useSocket.ts custom hook
const useSocket = (gameId: string) => {
  const [socket, setSocket] = useState<Socket | null>(null);
  const [gameState, setGameState] = useState<GameState | null>(null);
  
  useEffect(() => {
    const socketInstance = io(BACKEND_URL);
    socketInstance.emit('join-game', gameId);
    
    socketInstance.on('game-update', setGameState);
    socketInstance.on('error', handleError);
    
    return () => socketInstance.close();
  }, [gameId]);
};
```

#### 3.5 State Management
- **React Context**: Global game state and socket connection (with performance optimization using React.memo and selective context consumption)
- **Zustand/Jotai**: Consider for complex game state if Context performance becomes an issue
- **Local State**: UI-specific state (modals, forms)
- **Optimistic Updates**: Immediate UI feedback for actions
- **Error Handling**: Display validation errors from server

### Phase 4: Advanced Features & Polish (Week 4-5)
**Goal**: Implement complex game features and UI enhancements

#### 4.1 Side Pot Implementation
```typescript
interface SidePot {
  id: string;
  amount: number;
  eligiblePlayers: string[];
  winner?: string;
}

class SidePotService {
  calculateSidePots(players: Player[]): SidePot[] {
    // Complex side pot algorithm
  }
  
  distributeSidePots(sidePots: SidePot[], winners: WinnerInfo[]): void {
    // Distribute winnings across multiple pots
  }
}
```

#### 4.2 Enhanced UI Features
- **Animations**: Chip movement, card dealing effects using Framer Motion
- **Sound Effects**: Betting actions, win celebrations
- **Responsive Design**: Mobile-first approach with Tailwind CSS
- **Dark/Light Mode**: Theme switching with CSS variables

#### 4.3 Game Management Features
- **Pause/Resume**: Temporary game suspension
- **Player Substitution**: Replace disconnected players
- **Spectator Mode**: Watch mode for eliminated players
- **Game History**: View previous hands and actions

#### 4.4 Performance Optimization
- **React.memo**: Prevent unnecessary re-renders
- **useMemo/useCallback**: Optimize expensive calculations
- **Code Splitting**: Lazy load game components
- **Bundle Analysis**: Optimize build size with Vite

### Phase 5: Testing, Deployment & Monitoring (Week 5-6)
**Goal**: Production-ready deployment with comprehensive testing

#### 5.1 Testing Strategy
```typescript
// Backend testing
describe('GameService', () => {
  test('should handle betting rounds correctly', () => {
    // Unit tests for game logic
  });
});

// Frontend testing
describe('BettingControls', () => {
  test('should disable controls when not active player', () => {
    // Component testing with React Testing Library
  });
});

// E2E testing
describe('Full Game Flow', () => {
  test('should complete a full poker hand', () => {
    // Cypress or Playwright end-to-end tests
  });
});
```

#### 5.2 Performance Testing
- **Load Testing**: Artillery.js for concurrent game stress testing
- **Memory Profiling**: Redis memory usage monitoring
- **Database Performance**: MongoDB query optimization
- **Frontend Performance**: Lighthouse audits, Core Web Vitals

#### 5.3 Production Deployment
```bash
# Docker configuration
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
```

#### 5.4 Infrastructure Setup
- **Reverse Proxy**: Nginx for static file serving and load balancing
- **SSL/TLS**: Let's Encrypt certificate automation
- **Environment Configuration**: Production vs development settings
- **Process Management**: PM2 for Node.js process clustering

#### 5.5 Monitoring & Logging
- **Application Monitoring**: Winston logging with log levels
- **Error Tracking**: Sentry integration for error reporting
- **Performance Monitoring**: New Relic or DataDog APM
- **Database Monitoring**: Redis and MongoDB performance metrics

## Technical Specifications

### Socket.IO Event Architecture
```typescript
// Client to Server Events
interface ClientToServerEvents {
  'join-game': (gameId: string, playerName: string) => void;
  'leave-game': (gameId: string) => void;
  'betting-action': (gameId: string, action: BettingAction) => void;
  'start-game': (gameId: string) => void;
  'declare-winner': (gameId: string, winnerId: string) => void;
  'next-hand': (gameId: string) => void;
}

// Server to Client Events
interface ServerToClientEvents {
  'game-state-update': (gameState: GameState) => void;
  'player-joined': (player: Player) => void;
  'player-left': (playerId: string) => void;
  'betting-action-result': (result: ActionResult) => void;
  'error': (error: ErrorMessage) => void;
  'game-started': (gameState: GameState) => void;
  'hand-complete': (results: HandResults) => void;
}
```

### Redis Data Structure
```typescript
// Game state stored in Redis with JSON serialization strategy
interface RedisGameState {
  id: string;
  hostId: string;
  players: Record<string, Player>; // Changed from Map for JSON compatibility
  gameSettings: GameSettings;
  currentHand: HandState;
  potManager: PotManager;
  blindManager: BlindManager;
  actionHistory: Action[];
  createdAt: string; // ISO string for JSON compatibility
  lastActivity: string; // ISO string for JSON compatibility
}

// Redis keys pattern and storage strategy
const GAME_KEY = `game:${gameId}`;
const PLAYER_SESSION_KEY = `session:${playerId}`;
const GAME_PLAYERS_KEY = `game:${gameId}:players`; // Hash for atomic player updates
const ACTIVE_GAMES_SET = 'active-games';

// Redis storage methods
// - Game state: JSON.stringify/parse for full state
// - Player data: Redis Hashes for atomic updates (HSET game:id:players playerId data)
// - Session data: Simple key-value with TTL
```

### MongoDB Schemas
```typescript
// Game Settings Schema
const GameSettingsSchema = new Schema({
  blinds: { small: Number, big: Number },
  startingChips: Number,
  maxPlayers: Number,
  gameType: { type: String, enum: ['no-limit', 'pot-limit', 'limit'] }
});

// Player Result Schema
const PlayerResultSchema = new Schema({
  playerId: String,
  playerName: String,
  finalStack: Number,
  profit: Number,
  handsWon: Number,
  position: Number
});

// Hand Schema
const HandSchema = new Schema({
  handNumber: Number,
  dealerId: String,
  smallBlindId: String,
  bigBlindId: String,
  pot: Number,
  sidePots: [SidePotSchema],
  winnerId: String,
  winnings: Number,
  actionHistory: [ActionSchema],
  startTime: Date,
  endTime: Date
});

// Side Pot Schema
const SidePotSchema = new Schema({
  amount: Number,
  eligiblePlayers: [String],
  winnerId: String
});

// Action Schema
const ActionSchema = new Schema({
  playerId: String,
  type: { type: String, enum: ['fold', 'check', 'call', 'raise', 'all-in'] },
  amount: Number,
  timestamp: Date
});

// Game History Schema
const GameHistorySchema = new Schema({
  gameId: String,
  players: [PlayerResultSchema],
  hands: [HandSchema],
  finalResults: [PlayerResultSchema],
  gameSettings: GameSettingsSchema,
  startTime: Date,
  endTime: Date,
  duration: Number
});

// Player Statistics Schema
const PlayerStatsSchema = new Schema({
  playerId: String,
  playerName: String,
  gamesPlayed: Number,
  totalWinnings: Number,
  averageStack: Number,
  handsWon: Number,
  lastPlayed: Date
});
```

### React Component Architecture
```typescript
// Main Game Component Hierarchy
<GameProvider>
  <SocketProvider>
    <Router>
      <Routes>
        <Route path="/" element={<LobbyPage />} />
        <Route path="/game/:gameId" element={<GamePage />} />
        <Route path="/results/:gameId" element={<ResultsPage />} />
      </Routes>
    </Router>
  </SocketProvider>
</GameProvider>

// Game Page Structure
<GamePage>
  <GameHeader pot={pot} round={round} />
  <PlayersGrid>
    {players.map(player => 
      <PlayerCard 
        key={player.id} 
        player={player} 
        isCurrentPlayer={isCurrentPlayer}
        isDealer={isDealer}
      />
    )}
  </PlayersGrid>
  <BettingControls 
    currentPlayer={currentPlayer}
    gameState={gameState}
    onAction={handleBettingAction}
    disabled={!isMyTurn}
  />
  <GameActions>
    <StartHandButton />
    <DeclareWinnerButton />
    <PauseGameButton />
  </GameActions>
</GamePage>
```

### Game Flow Implementation
1. **Lobby Creation**: Host creates game with settings (blinds, starting chips)
2. **Player Joining**: Players join via unique game code using Socket.IO
3. **Game Start**: Host starts game, dealer/blind positions set in Redis
4. **Betting Rounds**: Players use individual devices for actions via WebSocket
5. **Hand Resolution**: Dealer declares winner, chips redistributed automatically
6. **Next Hand**: Automatic blind/dealer rotation, new hand begins
7. **Player Exit**: Real-time chip total calculation and display

### Winner Declaration Process
**Critical Design Decision**: Since cards are dealt physically, the system cannot automatically determine hand winners. The current dealer (player with dealer button) must declare the winner through the UI.

**Process Flow**:
1. After betting rounds complete, system waits for winner declaration
2. Only the current dealer can access winner declaration controls
3. Dealer selects winning player(s) from dropdown/interface
4. System validates and distributes pot/side pots automatically
5. All players see winner announcement and chip distribution
6. Next hand begins with automatic dealer rotation

**Trust & Dispute Considerations**:
- Clear UI indication of who can declare winners
- Winner declaration requires confirmation dialog
- Action is logged and visible to all players
- Future enhancement: Allow other players to contest declarations

### Data Models

#### Game State (TypeScript)
```typescript
interface GameState {
  id: string;
  hostId: string;
  players: Player[];
  currentDealer: string;
  blinds: { small: number; big: number };
  pot: number;
  sidePots: SidePot[];
  currentRound: 'preflop' | 'flop' | 'turn' | 'river';
  currentPlayer: string;
  roundBets: Record<string, number>;
  gamePhase: 'lobby' | 'playing' | 'paused' | 'finished';
  handNumber: number;
  actionHistory: Action[];
  lastAction?: Action;
  communityCards?: string[]; // Optional: for display reference only
}
```

#### Player State (TypeScript)
```typescript
interface Player {
  id: string;
  name: string;
  stack: number;
  status: 'active' | 'folded' | 'all-in' | 'eliminated' | 'away';
  currentBet: number;
  totalBetThisRound: number;
  isDealer: boolean;
  isSmallBlind: boolean;
  isBigBlind: boolean;
  position: number;
  lastAction?: BettingAction;
  socketId?: string;
  joinedAt: Date;
}
```

#### Betting Action (TypeScript)
```typescript
// Client-side betting action payload
interface ClientBettingAction {
  type: 'fold' | 'check' | 'call' | 'raise' | 'all-in';
  amount?: number;
}

// Server-processed betting action record
interface BettingActionRecord {
  type: 'fold' | 'check' | 'call' | 'raise' | 'all-in';
  amount?: number;
  playerId: string;
  timestamp: Date;
  isValid: boolean;
  error?: string;
}
```

### API Endpoints (Express.js)
```typescript
// RESTful API endpoints
app.post('/api/games', createGame);           // Create new game
app.get('/api/games/:gameId', getGameState);  // Get current game state
app.post('/api/games/:gameId/join', joinGame); // Join existing game
app.delete('/api/games/:gameId/leave', leaveGame); // Leave game
app.post('/api/games/:gameId/start', startGame);   // Start game
app.post('/api/games/:gameId/action', submitAction); // Submit betting action
app.post('/api/games/:gameId/declare-winner', declareWinner); // Declare hand winner (dealer only)
app.post('/api/games/:gameId/next', nextHand);     // Start next hand

// Admin/utility endpoints
app.get('/api/games/:gameId/history', getGameHistory);
app.post('/api/games/:gameId/pause', pauseGame);
app.post('/api/games/:gameId/resume', resumeGame);
```

### Security Implementation
```typescript
// Rate limiting middleware
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // limit each IP to 100 requests per windowMs
  message: 'Too many requests from this IP'
});

// Input validation middleware
const validateBettingAction = (req: Request, res: Response, next: NextFunction) => {
  const { action, amount } = req.body;
  
  // Validate action type
  if (!['fold', 'check', 'call', 'raise', 'all-in'].includes(action)) {
    return res.status(400).json({ error: 'Invalid action type' });
  }
  
  // Validate bet amount for raise actions
  if (action === 'raise' && (!amount || amount <= 0)) {
    return res.status(400).json({ error: 'Invalid raise amount' });
  }
  
  next();
};

// CORS configuration
const corsOptions = {
  origin: process.env.FRONTEND_URL || 'http://localhost:5173',
  credentials: true
};
```

### Performance Considerations
- **Redis TTL**: Game states expire after 24 hours of inactivity
- **Connection Pooling**: MongoDB connection pool size: 10
- **Socket.IO Scaling**: Redis adapter for multi-server deployment
- **React Optimization**: useMemo for expensive calculations, React.memo for components
- **Bundle Splitting**: Lazy load game components to reduce initial bundle size
- **CDN**: Serve static assets from CDN in production

## Game Configuration

### Tech Stack
1. **Frontend Framework**: React 18 with TypeScript, Bootstrap for styling
2. **Backend Technology**: Node.js with Express.js and TypeScript
3. **Database**: Redis (game state) + MongoDB (persistence)
4. **Real-time**: WebSockets with Socket.IO

### Game Rules & Configuration
1. **Blind Structure**: Fixed blinds per game (configurable at game creation)
2. **Player Limits**: Maximum 10 players per game (Texas Hold'em standard)
3. **Betting Rules**: No-limit betting with minimum bet = big blind
4. **Game Variations**: No-limit Texas Hold'em (future: pot-limit, limit options)

### User Experience
1. **Authentication**: Anonymous sessions with player names
2. **Game Persistence**: Games survive server restarts via Redis persistence  
3. **Mobile Features**: PWA capabilities, responsive design
4. **Accessibility**: Screen reader support, keyboard navigation

**Session Management**: Players receive a session token upon joining, stored in localStorage. Socket.IO events include session validation to ensure players can only act for themselves.

### Deployment
1. **Hosting Platform**: Docker containers (platform agnostic)
2. **Domain**: Custom domain with SSL
3. **SSL Requirements**: Let's Encrypt certificate automation
4. **Monitoring**: Winston logging, Sentry error tracking

## Development Environment Setup

### Prerequisites
- Node.js 18+ and npm
- Redis server
- MongoDB instance
- Git for version control

### Local Development Commands
```bash
# Backend setup
cd chip-champ-backend
npm install
npm run dev

# Frontend setup  
cd chip-champ-frontend
npm install
npm run dev

# Database setup
docker run -d --name redis -p 6379:6379 redis:alpine
docker run -d --name mongo -p 27017:27017 mongo:latest
```

### Project Structure
```
chip-champ-service/
├── backend/                 # Node.js Express API
│   ├── src/
│   │   ├── controllers/    # Express route handlers
│   │   ├── services/       # Business logic
│   │   ├── models/         # Data models and schemas
│   │   ├── middleware/     # Express middleware
│   │   ├── routes/         # API route definitions
│   │   ├── socket/         # Socket.IO event handlers
│   │   └── utils/          # Helper functions
│   ├── tests/              # Backend tests
│   ├── package.json
│   └── tsconfig.json
├── frontend/               # React TypeScript app
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── hooks/          # Custom React hooks
│   │   ├── services/       # API and Socket services
│   │   ├── types/          # TypeScript interfaces
│   │   ├── context/        # React Context providers
│   │   └── utils/          # Helper functions
│   ├── public/             # Static assets
│   ├── package.json
│   └── vite.config.ts
├── shared/                 # Shared TypeScript types
├── docs/                   # Documentation
└── docker-compose.yml      # Local development setup
```

## Success Metrics
- Smooth real-time synchronization across all devices
- Accurate side pot calculations in complex scenarios
- Intuitive mobile interface for all betting actions
- Zero data loss during player connections/disconnections
- Fast game creation and joining process (< 30 seconds)

---

*Development plan to be updated during development to keep track of what has been made and what will continue to be made.*