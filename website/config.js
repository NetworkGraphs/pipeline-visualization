import {readFile} from 'fs/promises'
import {join} from 'path'
import yaml from 'js-yaml'

async function load_yaml_abs(abs_path){
    const fileContent = await readFile(abs_path,'utf-8')
    const data = yaml.load(fileContent);
    return data;
}

const webdir = process.cwd()
const rootdir = join(webdir,"..")
const cachedir = join(rootdir,"cache")
const manifets = await load_yaml_abs(join(rootdir,"manifest.yaml"))
const outdir = join(cachedir,"web")
const base = manifets.website.base

const config = {
    rootdir,
    base,
    cachedir,
    outDir: outdir,
}

console.log(config)

export {
    config
}
