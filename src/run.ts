import * as fs from "fs";
import matter from "gray-matter";
import * as Cluster from "cluster";
import {text} from "stream/consumers";
import {writeFileSync} from "fs";
import {it} from "node:test";

const SOLUTION_DIRS = ['./leetCode']

type Difficultly = "easy" | "medium" | "hard"
interface Solution {
    title: string
    number?: number
    solved: boolean
    path:string
    difficulty: Difficultly
    tags:string[]
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

const getIcon = (difficulty:Difficultly)=>{
    switch (difficulty) {
        case "easy":return `:white_circle:`
        case "medium":return ":large_blue_circle:"
        case "hard":return ":red_circle:"
    }
}

function writeReadme(solutions: Solution[]){
    const intro = fs.readFileSync('./intro.md',{encoding: "utf-8"})
    let result = intro+ "\n\n"+"### Problems solved\n"
    const solutionsSolved = solutions.filter((item)=> item.solved)
    // Problems solved
    const numEasy = solutionsSolved.filter((item)=> item.difficulty === 'easy').length
    result += `\n${getIcon("easy")} Easy: ${numEasy}\n`
    const numMedium = solutionsSolved.filter((item)=> item.difficulty === 'medium').length
    result += `\n:${getIcon("medium")} Medium: ${numMedium}\n`
    const numHard = solutionsSolved.filter((item)=>  item.difficulty === 'hard').length
    result += `\n${getIcon('hard')} Hard: ${numHard}\n`
    result +=`\n__Total__: ${solutionsSolved.length}\n`
    // Iterate through solutions
    result += '\n### Solutions\n\n'
    solutions.sort((a,b)=> (a.number || 0) - (b.number || 0))
    let index = 1
    const tags:Record<string, number> = {}
    for (const solution of solutionsSolved){
        result+= `${index}. ${getIcon(solution.difficulty || 'easy')} [${solution.title}](${solution.path})\n`
        index+=1
        solution.tags.forEach((item)=>{
            if(item in tags){
                tags[item] +=1
            }else{
                tags[item]= 1
            }
        })
    }
    // Write tags
    const tagsArraySorted = Object.keys(tags).map((item)=>({name: item,count: tags[item]}))
    result += "\n### Tags by count\n\n"
    index = 1
    tagsArraySorted.sort((a,b)=> b.count-a.count)
    for (const tag of tagsArraySorted){
        result += `${index}. **${tag.name}**: ${tag.count}\n\n`
        index+=1
    }
    writeFileSync("./README1.md",result)

}


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
        writeReadme(solutions)
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
