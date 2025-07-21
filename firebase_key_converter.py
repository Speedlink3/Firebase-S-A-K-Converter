# Create `lib/` folder if not exists and write firebase.ts and firebaseAdmin.ts
lib_path = os.path.join(extracted_folder_path, "lib")
os.makedirs(lib_path, exist_ok=True)

# firebase.ts content (client side Firebase initialization)
firebase_ts_content = """
import { initializeApp, getApps, getApp } from 'firebase/app';

const firebaseConfig = {
  apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY,
  authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
  projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
  storageBucket: process.env.NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: process.env.NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID,
  appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID,
};

const app = getApps().length ? getApp() : initializeApp(firebaseConfig);
export default app;
"""

# firebaseAdmin.ts content (server side Firebase Admin SDK)
firebase_admin_ts_content = """
import * as admin from 'firebase-admin';

const serviceAccount = JSON.parse(process.env.FIREBASE_SERVICE_ACCOUNT_KEY || '{}');

if (!admin.apps.length) {
  admin.initializeApp({
    credential: admin.credential.cert(serviceAccount),
  });
}

export const db = admin.firestore();
export const auth = admin.auth();
"""

# Write the files
with open(os.path.join(lib_path, "firebase.ts"), "w") as f:
    f.write(firebase_ts_content.strip())

with open(os.path.join(lib_path, "firebaseAdmin.ts"), "w") as f:
    f.write(firebase_admin_ts_content.strip())

# Confirm files created
os.listdir(lib_path)
