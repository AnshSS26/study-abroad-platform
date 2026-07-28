"use client";

import { useState } from "react";


type Recommendation = {
  university: string;
  program: string;
  country: string;
  city: string;
  tuition_fee: number | null;
  currency: string | null;
  scholarship: string | null;
  match_score: number;
  reasons: string[];
};


export default function Home() {


  const [formData, setFormData] = useState({

    name: "",
    email: "",

    preferred_country: "",
    preferred_course: "",

    maximum_budget: "",
    budget_currency: "USD",

    cgpa: "",
    ielts: "",

  });



  const [results, setResults] =
    useState<Recommendation[]>([]);


  const [loading, setLoading] =
    useState(false);


  const [error, setError] =
    useState("");





  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>
  ) => {


    setFormData({

      ...formData,

      [e.target.name]:
        e.target.value,

    });


  };






  async function handleSubmit(
    e: React.FormEvent
  ) {


    e.preventDefault();


    setLoading(true);

    setError("");

    setResults([]);




    try {



      // Save student profile

      const profileResponse = await fetch(

        "https://study-abroad-platform-lpbo.onrender.com/students",

        {

          method: "POST",

          headers: {

            "Content-Type":
              "application/json",

          },


          body: JSON.stringify({

            name:
              formData.name,


            email:
              formData.email,


            preferred_country:
              formData.preferred_country,


            preferred_course:
              formData.preferred_course,


            budget:
              Number(formData.maximum_budget),


            currency:
              formData.budget_currency,


            cgpa:
              Number(formData.cgpa),


            ielts:
              Number(formData.ielts),


          }),


        }

      );



      if (!profileResponse.ok) {

        throw new Error(
          "Profile save failed"
        );

      }





      // Get recommendations


      const response = await fetch(

        "https://study-abroad-platform-lpbo.onrender.com/recommend",

        {


          method: "POST",


          headers: {


            "Content-Type":
              "application/json",


          },


          body: JSON.stringify({


            preferred_country:
              formData.preferred_country,


            preferred_course:
              formData.preferred_course,


            maximum_budget:
              Number(formData.maximum_budget),


            budget_currency:
              formData.budget_currency,


            cgpa:
              Number(formData.cgpa),


            ielts:
              Number(formData.ielts),


          }),


        }

      );





      const data =
        await response.json();




      if (!response.ok) {


        throw new Error(
          "Recommendation failed"
        );


      }





      setResults(data);




    } catch (error) {


      setError(
        "Unable to connect with recommendation service."
      );


    }





    setLoading(false);


  }






  return (

    <main className="min-h-screen bg-gradient-to-br from-blue-50 to-white p-8">


      <div className="max-w-6xl mx-auto">



        <h1 className="text-4xl font-bold">

          AI Study Abroad Advisor

        </h1>



        <p className="mt-3 text-gray-600 text-lg">

          Find universities based on your profile,
          budget and goals.

        </p>





        <form


          onSubmit={handleSubmit}


          className="bg-white shadow-xl rounded-2xl p-8 mt-8 space-y-6"


        >



          <div>

            <label className="font-semibold">

              Name

            </label>


            <input

              name="name"

              value={formData.name}

              onChange={handleChange}

              placeholder="Your name"

              className="w-full border rounded-lg p-3 mt-2"

              required

            />


          </div>




          <div>

            <label className="font-semibold">

              Email

            </label>


            <input

              type="email"

              name="email"

              value={formData.email}

              onChange={handleChange}

              placeholder="Email address"

              className="w-full border rounded-lg p-3 mt-2"

              required

            />


          </div>
                    <div>

            <label className="font-semibold">

              Preferred Country

            </label>


            <select

              name="preferred_country"

              value={formData.preferred_country}

              onChange={handleChange}

              className="w-full border rounded-lg p-3 mt-2"

              required

            >

              <option value="">
                Select country
              </option>

              <option>
                United States
              </option>

              <option>
                Canada
              </option>

              <option>
                United Kingdom
              </option>

              <option>
                Australia
              </option>


            </select>


          </div>





          <div>


            <label className="font-semibold">

              Target Program

            </label>


            <input

              name="preferred_course"

              value={formData.preferred_course}

              onChange={handleChange}

              placeholder="Example: M.S. Computer Science"

              className="w-full border rounded-lg p-3 mt-2"

              required

            />


          </div>





          <div className="grid md:grid-cols-3 gap-4">


            <input

              type="number"

              name="maximum_budget"

              value={formData.maximum_budget}

              onChange={handleChange}

              placeholder="Budget"

              className="border rounded-lg p-3"

              required

            />



            <select

              name="budget_currency"

              value={formData.budget_currency}

              onChange={handleChange}

              className="border rounded-lg p-3"

            >

              <option>
                USD
              </option>

              <option>
                CAD
              </option>

              <option>
                GBP
              </option>


            </select>




            <input

              type="number"

              step="0.1"

              name="cgpa"

              value={formData.cgpa}

              onChange={handleChange}

              placeholder="CGPA"

              className="border rounded-lg p-3"

              required

            />


          </div>





          <input

            type="number"

            step="0.5"

            name="ielts"

            value={formData.ielts}

            onChange={handleChange}

            placeholder="IELTS Score"

            className="w-full border rounded-lg p-3"

            required

          />





          <button

            type="submit"

            className="bg-blue-600 hover:bg-blue-700 text-white font-bold px-8 py-3 rounded-xl"

          >

            {
              loading
              ? "Analyzing Universities..."
              : "Find My Universities"
            }


          </button>




          {

            error &&

            <p className="text-red-600">

              {error}

            </p>

          }





        </form>





        {

          results.length > 0 &&


          <section className="mt-10">


            <h2 className="text-3xl font-bold mb-6">

              AI Recommended Universities

            </h2>





            <div className="space-y-6">


              {

                results.map((item,index)=>(


                  <div

                    key={index}

                    className="bg-white rounded-2xl shadow-lg p-6 border"

                  >




                    <div className="flex justify-between">


                      <div>


                        <h3 className="text-2xl font-bold">

                          {item.university}

                        </h3>


                        <p className="text-gray-600">

                          {item.city}, {item.country}

                        </p>


                      </div>





                      <div className="bg-green-100 text-green-700 px-4 py-2 rounded-full font-bold h-fit">

                        {item.match_score}% Match

                      </div>


                    </div>





                    <div className="mt-5 space-y-2">


                      <p>

                        <b>Program:</b> {item.program}

                      </p>


                      <p>

                        <b>Tuition:</b>{" "}

                        {item.currency ?? ""}

                        {" "}

                        {item.tuition_fee ?? "Not available"}

                      </p>


                      <p>

                        <b>Scholarship:</b>{" "}

                        {item.scholarship ?? "Not available"}

                      </p>


                    </div>






                    <div className="mt-5">


                      <h4 className="font-bold">

                        Why this university?

                      </h4>


                      <ul className="list-disc ml-6 mt-2">


                        {

                          item.reasons?.map(

                            (reason,i)=>(

                              <li key={i}>

                                {reason}

                              </li>

                            )

                          )

                        }


                      </ul>


                    </div>




                  </div>


                ))

              }



            </div>


          </section>


        }





      </div>


    </main>


  );


}