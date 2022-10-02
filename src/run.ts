import * as fs from "fs";
import matter from "gray-matter";
import * as Cluster from "cluster";
import {text} from "stream/consumers";

const SOLUTION_DIRS = ['./leetCode']

interface Solution {
    title: string
    number?: number
    solved: boolean
    path:string
    difficulty: string
    tags:string
    provider:string
}

const getFilesInDir = (path:string):string[]=>{
    const results:string[] = []
    const files = fs.readdirSync(path,{withFileTypes:true})
    for (const item of files){
        if (item.isDirectory()){
            results.push(...getFilesInDir(path+"/"+item.name))
        }else{
            results.push(path+ "/" + item.name)
        }
    }
    return results
}

const capitalize = (input:string)=>{
    return input
        .split(" ")
        .map((word)=>{
            return word[0].toUpperCase()+word.substring(1)
        }).join(" ")
}

const DOCSTRING_METADATA_REGEX = '"""[\\s\\S]*?"""'
const metadataRegex = new RegExp(DOCSTRING_METADATA_REGEX)
function main() {
    const solutions: Solution[] = []
    for (const parentPath of SOLUTION_DIRS) {
        const files = getFilesInDir(parentPath)
        for (const filePath of files) {
            const file = fs.readFileSync(filePath, {encoding: "utf-8"})
            const result = file.match(metadataRegex)
            if (result){
                const metaString = result[0]
                const sliced = metaString.slice(4,metaString.length-4)
                const metadata = matter(sliced).data
                if (metadata.title){
                    solutions.push({
                        path: filePath,
                        ...(metadata.title && {title: capitalize(metadata.title)}),
                        ...(metadata.difficulty && {difficulty: metadata.difficulty.toLowerCase()}),
                        ...(metadata.number && {number: metadata.number}),
                        ...(metadata.tags && {tags: (metadata.tags as string[]).map((item)=> capitalize(item))}),
                        solved: !!metadata.solved,
                        provider: parentPath.split("./")[1].toUpperCase()
                    })
                }
            }
        }
        console.log("gotovi")
        fs.writeFileSync("solutions.json",JSON.stringify(solutions))
    }

}
   // const filePath = './leetCode/1_two_sum.py'
    // const file = fs.readFileSync(filePath,{encoding: "utf-8"})
    // const result = file.match(metadataRegex)
    // if(result){
    //     const textString = result[0]
    //     const sliced = textString.slice(4,textString.length-4)
    //     const metadata = matter(sliced).data
    //     console.log("dsa")
    // }

main()
