import {join} from 'path'
import {loadEnv} from 'vite'

const webdir = process.cwd()
const env = loadEnv("",webdir,"PUBLIC_BASE")
const rootdir = join(webdir,"..")
const cachedir = join(rootdir,"cache")
const outdir = join(cachedir,"web")
const base = env.PUBLIC_BASE

const config = {
    webdir,
    rootdir,
    base,
    cachedir,
    outDir: outdir,
}

console.log(config)

export {
    config
}
