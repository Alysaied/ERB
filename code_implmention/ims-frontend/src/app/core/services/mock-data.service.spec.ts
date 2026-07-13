import { TestBed } from '@angular/core/testing';
import { provideRouter } from '@angular/router';
import { MockDataService } from './mock-data.service';

describe('MockDataService', () => {
  let service: MockDataService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [MockDataService, provideRouter([])],
    });
    service = TestBed.inject(MockDataService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should return screen data for UI-002', () => {
    const data = service.getScreenData('UI-002') as { kpis: unknown[] };
    expect(data.kpis).toBeDefined();
    expect(data.kpis.length).toBeGreaterThan(0);
  });

  it('should return products', () => {
    const products = service.getProducts();
    expect(products.length).toBeGreaterThan(0);
  });
});
