import '@/styles/globals.css'
import Head from 'next/head'

export default function App({ Component, pageProps }) {
  return <>
    <Head>
        <title>Securin Interview: Saransh Saini (+918178703402)</title>
        <meta name="description" content="My technical interview at Securin." />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/science_logo.png" />
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500&display=swap" rel="stylesheet" />
    </Head>
    <Component {...pageProps} />
  </>
  
}