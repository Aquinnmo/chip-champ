// Jest test setup file
// This file runs before each test suite

// Set test environment variables
process.env.NODE_ENV = 'test';
process.env.PORT = '3001';

// Increase timeout for integration tests
jest.setTimeout(10000);

// Mock console methods for cleaner test output (optional)
// Uncomment if you want to suppress console.log during tests
// global.console = {
//   ...console,
//   log: jest.fn(),
//   error: jest.fn(),
//   warn: jest.fn(),
// };
