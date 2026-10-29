export const imageConfig = {
  // Enhanced image optimization settings
  limitInputPixels: 268402689, // ~16K x 16K pixels
  jpeg: {
    quality: 85,
    progressive: true,
    optimizeScans: true,
    mozjpeg: true
  },
  png: {
    quality: 85,
    progressive: true,
    compressionLevel: 9,
    adaptiveFiltering: true
  },
  webp: {
    quality: 80,
    lossless: false,
    smartSubsample: true,
    effort: 5
  },
  avif: {
    quality: 85,
    lossless: false,
    speed: 5
  }
}
