import React from 'react'
import styler from "../styles/Index.module.css"
import { useEffect, useState } from 'react'
import Image from 'next/image'
import Link from 'next/link'

const index = () => {
  const [recipes, setRecipes] = useState([])
  useEffect(() => {
    fetch(`http://127.0.0.1:5000/api/recipes?limit=1&page=2`).then((a) => {
      return a.json()
    }).then((res) => {
        console.log(res)
        setRecipes(res)
    })
  }, [])
  return (
    <>
      <section className={styler.pageHeader}>
        <div className={styler.head} style={{marginTop:"5rem"}}>Securin Inteview</div>
        <div className={styler.headCont} style={{fontSize:"5rem",fontWeight:"600",marginTop:"1rem",paddingBottom:"1rem"}}>Recipe Fetcher App</div>
        {/* <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -50 1440 320" className={styler.path1}><path style={{marginTop:"5rem"}} fill="#ffffff" fill-opacity="1" d="M0,160L40,144C80,128,160,96,240,85.3C320,75,400,85,480,117.3C560,149,640,203,720,224C800,245,880,235,960,213.3C1040,192,1120,160,1200,149.3C1280,139,1360,149,1400,154.7L1440,160L1440,320L1400,320C1360,320,1280,320,1200,320C1120,320,1040,320,960,320C880,320,800,320,720,320C640,320,560,320,480,320C400,320,320,320,240,320C160,320,80,320,40,320L0,320Z"></path></svg> */}
      </section>
      <section className={styler.tableSection}>
        
      </section>
    </>
  )
}

export default index