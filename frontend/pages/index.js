import React from "react";
import styler from "../styles/Index.module.css";
import { useEffect, useState } from "react";
import Image from "next/image";
import Link from "next/link";

const index = () => {
  const [recipes, setRecipes] = useState([]);
  const [element, setElement] = useState(["sweet"]);
  const [extra, setExtra] = useState([]);
  const [showModal, setShowModal] = useState(false);
  useEffect(() => {
    fetch(`http://127.0.0.1:5000/api/recipes?limit=10&page=2`)
      .then((a) => {
        return a.json();
      })
      .then((res) => {
        setRecipes(res);
      });
  }, []);
  useEffect(() => {
    fetch(`http://127.0.0.1:5000/api/recipes/search?title=${element}`)
      .then((a) => {
        return a.json();
      })
      .then((res) => {
        setExtra(res[0]);
      });
  }, [element]);
  return (
    <>
      <section className={styler.pageHeader}>
        <div className={styler.head} style={{ marginTop: "1rem" }}>
          Securin Inteview
        </div>
        <div
          className={styler.headCont}
          style={{
            fontSize: "5rem",
            fontWeight: "600",
            marginTop: "1rem",
            paddingBottom: "1rem",
          }}
        >
          Recipe Fetcher App
        </div>
        {/* <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -50 1440 320" className={styler.path1}><path style={{marginTop:"5rem"}} fill="#ffffff" fill-opacity="1" d="M0,160L40,144C80,128,160,96,240,85.3C320,75,400,85,480,117.3C560,149,640,203,720,224C800,245,880,235,960,213.3C1040,192,1120,160,1200,149.3C1280,139,1360,149,1400,154.7L1440,160L1440,320L1400,320C1360,320,1280,320,1200,320C1120,320,1040,320,960,320C880,320,800,320,720,320C640,320,560,320,480,320C400,320,320,320,240,320C160,320,80,320,40,320L0,320Z"></path></svg> */}
      </section>

      {showModal && (
        <section className={styler.description}>
          <div className={styler.extraInfo}>
            <p className={styler.info} style={{ fontSize: "2rem" }}>
              {extra.title}
            </p>
            <p className={styler.info}>Desciption : {extra.description}</p>
            <p className={styler.info}>Total Time : {extra.total_time}</p>
            <div className={styler.info}>
              <p className={styler.info}>Nutrients</p>
              <table className={styler.nutriTable} style={{ width: "100%", border: "1px solid black" }}>
                <thead>
                    <tr className={styler.trowrewr}>
                        <td className={styler.tdaeare}>Calories</td>
                        <td className={styler.tdaeare}>Carbohydrate Content</td>
                        <td className={styler.tdaeare}>Cholesterol Content</td>
                        <td className={styler.tdaeare}>Fiber Content</td>
                        <td className={styler.tdaeare}>Protein Content</td>
                        <td className={styler.tdaeare}>Saturated Fat Content</td>
                        <td className={styler.tdaeare}>Sodium Content</td>
                        <td className={styler.tdaeare}>Sugar Content</td>
                        <td className={styler.tdaeare}>Fat Content</td>
                    </tr>
                </thead>
                <tbody>
                    <tr className={styler.trowrewr}>
                        <td className={styler.tdaeare}>{extra.nutrients.calories}</td>
                        <td className={styler.tdaeare}>{extra.nutrients.carbohydrateContent}</td>
                        <td className={styler.tdaeare}>{extra.nutrients.cholesterolContent}</td>
                        <td className={styler.tdaeare}>{extra.nutrients.fiberContent}</td>
                        <td className={styler.tdaeare}>{extra.nutrients.proteinContent}</td>
                        <td className={styler.tdaeare}>{extra.nutrients.saturatedFatContent}</td>
                        <td className={styler.tdaeare}>{extra.nutrients.sodiumContent}</td>
                        <td className={styler.tdaeare}>{extra.nutrients.sugarContent}</td>
                        <td className={styler.tdaeare}>{extra.nutrients.fatContent}</td>
                    </tr>
                </tbody>
              </table>
            </div>
          </div>
        </section>
      )}
      <section className={styler.tableSection}>
        <table className={styler.tableContent}>
          <thead className={styler.thead}>
            <tr className={styler.trow}>
              <td className={styler.tdata}>Title</td>
              <td className={styler.tdata}>Cuisine</td>
              <td className={styler.tdata}>Rating</td>
              <td className={styler.tdata}>Total Time</td>
              <td className={styler.tdata}>No. of People Serves</td>
              <td className={styler.tdata}>Calories</td>
            </tr>
          </thead>
          <tbody className={styler.tbody}>
            {recipes.map((recipe, index) => {
              return (
                <>
                  <tr
                    className={styler.trow}
                    onClick={() => {
                      setElement(recipe.title);
                      setShowModal(true);
                    }}
                    key={index}
                  >
                    <td className={styler.tdata}>{recipe.title}</td>
                    <td className={styler.tdata}>{recipe.cuisine}</td>
                    <td className={styler.tdata}>{recipe.rating}</td>
                    <td className={styler.tdata}>{recipe.total_time}</td>
                    <td className={styler.tdata}>{recipe.serves}</td>
                    <td className={styler.tdata}>
                      {recipe.nutrients.calories}
                    </td>
                  </tr>
                </>
              );
            })}
          </tbody>
        </table>
      </section>
    </>
  );
};

export default index;
