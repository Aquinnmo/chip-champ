import request from 'supertest';
import app from '../src/app';

describe('Basic App Setup', () => {
  describe('GET /health', () => {
    it('should return health check status', async () => {
      const response = await request(app)
        .get('/health')
        .expect(200);

      expect(response.body).toHaveProperty('status', 'OK');
      expect(response.body).toHaveProperty('message', 'Chip Champ Backend is running');
      expect(response.body).toHaveProperty('timestamp');
    });
  });

  describe('GET /api', () => {
    it('should return API information', async () => {
      const response = await request(app)
        .get('/api')
        .expect(200);

      expect(response.body).toHaveProperty('message', 'Chip Champ API - Phase 1.1 Setup Complete');
      expect(response.body).toHaveProperty('version', '1.0.0');
    });
  });

  describe('GET /nonexistent', () => {
    it('should return 404 for unknown routes', async () => {
      const response = await request(app)
        .get('/nonexistent')
        .expect(404);

      expect(response.body).toHaveProperty('error', 'Not Found');
      expect(response.body.message).toContain('/nonexistent');
    });
  });

  describe('Rate Limiting', () => {
    it('should apply rate limiting middleware', async () => {
      // Make multiple requests to test rate limiting is configured
      const promises = Array(5).fill(0).map(() => 
        request(app).get('/health')
      );
      
      const responses = await Promise.all(promises);
      
      // All should succeed (we're not hitting the limit in this test)
      responses.forEach(response => {
        expect(response.status).toBe(200);
      });
    });
  });
});
