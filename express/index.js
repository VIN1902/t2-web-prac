import express from "express"

const app = express()
const port = 3000

app.use(express.json())

const courses = [
    {id: 1, name: "course 1"},
    {id: 2, name: "course 2"},
    {id: 3, name: "course 3"},
    {id: 4, name: "course 4"},
    {id: 5, name: "course 5"},
]

app.get('/api/courses', (req, res)=>{
    res.send(courses)
})

app.get('/api/courses/:id', (req, res)=>{
    let getCourse = courses.find((x)=>x.id === Number(req.params.id))
    if (!getCourse) {
        res.status(404).json({
            'message': 'not found'
        })
        console.log(getCourse)
    } else {
        res.send(getCourse)
    }
})

app.post('/api/courses', (req, res)=>{
    const course = {
        id: courses.length + 1,
        name: req.body.name
    }
    courses.push(course)
    res.send(courses)
})

app.put('/api/courses/:id', (req, res)=>{
    let updateCourse = courses.find((x)=>x.id === Number(req.params.id))
    if(!updateCourse){
        res.status(404).json({
            "message": "not found"
        })
    } else {
        updateCourse.name = req.body.name
        res.send(courses)
    }
})

app.delete('/api/courses/:id', (req, res)=>{
    let deleteCourse = courses.find((x)=>x.id === Number(req.params.id))
    if(!deleteCourse){
        res.status(404).json({
            "message": "not found"
        })
    } else {
        const index = courses.indexOf(deleteCourse)
        courses.splice(index, 1)
        res.send(courses)
    }
})

app.listen(port, ()=>{
    console.log("listening at port", port)
})