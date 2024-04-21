import { defineConfig } from 'astro/config';
import {config} from './config.js'

// https://astro.build/config
export default defineConfig({
    output: 'static',
    outDir: config.outDir,
    base: config.base
});
