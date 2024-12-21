import Link from 'next/link';

export default function Home() {
  return (
    <div>
      <h1>Welcome to Mofa's Kitchen Buddy</h1>
      <nav>
        <ul>
          <li><Link href="/ingredients">Manage Ingredients</Link></li>
          <li><Link href="/recipes">View Recipes</Link></li>
          <li><Link href="/chatbot">Chat with Bot</Link></li>
        </ul>
      </nav>
    </div>
  );
}