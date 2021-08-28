import { useEffect, useState } from 'react'
import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'
import CloudUploadIcon from '@material-ui/icons/CloudUpload'
import Button from '@material-ui/core/Button';
import { Viewer } from '@react-pdf-viewer/core';
import { Worker } from '@react-pdf-viewer/core';
import axios from 'axios';

export default function Home() {
  const [selectedFile, setSelectedFile] = useState(undefined)
  const [url, setUrl] = useState('');
  const [codeResponse, seCodeResponse] = useState('');
  
  const onFileChange = event => { 
    // Update the state 
    setSelectedFile(event.target.files[0])
    setUrl(URL.createObjectURL(event.target.files[0]))
    onFileUpload(event.target.files[0])
  }

  const onFileUpload = async (file) => { 
    // Create an object of formData 
    const formData = new FormData(); 
   
    // Update the formData object 
    formData.append( 
      "file", 
      file
    ); 
   
    // Details of the uploaded file 
    console.log(file); 
   
    // Request made to the backend api 
    // Send formData object 
    const resp = await axios.post("http://localhost:8000/api/extract/file", formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
    console.log(resp.data)
    seCodeResponse(JSON.stringify(resp.data,null,'\t'))
  }; 


  return (
    <div className={styles.container}>
      <Head>
        <title>PRGX BACKEND</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>
          Welcome to <a href="https://www.prgx.com/">Prgx!</a>
        </h1>

        <p className={styles.description}>
          Please select a file
        </p>

        <div className={styles.grid}>    
          {selectedFile ? (
            <div
              style={{border: '1px solid rgba(0, 0, 0, 0.3)', height: '500px', width: '400px'}}
              className={styles.card}
            >
              <Worker workerUrl="https://unpkg.com/pdfjs-dist@2.6.347/build/pdf.worker.min.js">
                <Viewer fileUrl={url} />
              </Worker>
            </div>) : (
              <div>
                <input type="file" accept=".pdf" onChange={onFileChange} />
              </div>
            )
          }
          {codeResponse &&
            <div className={styles.card}>
              <p className={styles.description}>
                Response : {' '}
                <code className={styles.code}>{codeResponse}</code>
              </p>
            </div>
          }
        </div>
      </main>

      <footer className={styles.footer}>
        <a
          href="https://www.prgx.com/"
          target="_blank"
          rel="noopener noreferrer"
        >
          Powered by{' '}
          Prgx!
        </a>
      </footer>
    </div>
  )
}
