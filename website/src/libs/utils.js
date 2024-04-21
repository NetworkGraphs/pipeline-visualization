import { config } from "@/config";
import {readFile} from 'fs/promises'
import {join} from 'path'

async function load_yaml_abs(abs_path){
    const fileContent = await readFile(abs_path,'utf-8')
    const data = yaml.load(fileContent);
    return data;
}

async function load_yaml(path,folder="cachedir"){
    return await load_yaml_abs(join(config[folder],path));
}

async function load_json(path,folder="cachedir"){
    const abs_path = join(config[folder],path)
    const text = await readFile(abs_path,'utf-8')
    return JSON.parse(text)
  }
  
async function load_text(path,folder="cachedir"){
    return await readFile(join(config[folder],path));
}

export{
    load_yaml,
    load_text,
    load_json
}
