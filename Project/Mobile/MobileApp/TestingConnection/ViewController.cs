using System;
using System.Net;
using System.IO;
using System.Text;
using UIKit;
using SystemConfiguration;
using System.Net.Http;
using CoreFoundation;

namespace TestingConnection
{
	public partial class ViewController : UIViewController
	{
		protected ViewController(IntPtr handle) : base(handle)
		{
			// Note: this .ctor should not contain any initialization logic.
		}

		public override void ViewDidLoad()
		{
			base.ViewDidLoad();
			// Perform any additional setup after loading the view, typically from a nib.
			// http://192.168.99.100:8080/#/home/api/login
			// http://192.168.99.100:8080/#/home
			// http://192.168.99.100:8080/api/messages

			NetworkReachabilityFlags flags = 0;// = NetworkReachabilityFlags.ConnectionOnTraffic;
			NetworkReachability reachability = new NetworkReachability("http://192.168.99.100:8080/api/message");

			// Need to probe before we queue, or we wont get any meaningful values
			// this only happens when you create NetworkReachability from a hostname
			reachability.TryGetFlags(out flags);
			Console.WriteLine("New state for host: " + flags);
			//reachability.SetNotification(OnChange);
			reachability.Schedule(CFRunLoop.Current, CFRunLoop.ModeDefault);

			// Create a request using a URL that can receive a post.   
			WebRequest request = WebRequest.Create("http://192.168.99.100:8080/api/message");
			// Set the Method property of the request to POST.  
			request.Method = "POST";
			request.ContentType = "application/json";
			//request.Headers = new WebHeaderCollection().Add(HttpRequestHeader.Accept., "new");

			//string postData = "my data";
			//byte[] byte1 = Encoding.ASCII.GetBytes("{\"1\":\"hello from kim\"}");

			// Set the content type of the data being posted.


			ASCIIEncoding encoding = new ASCIIEncoding();
			Byte[] bytes = encoding.GetBytes("{\"id\":\"1\",\"mess\":\"hello from kim\"}");

			Stream newStream = request.GetRequestStream();
			newStream.Write(bytes, 0, bytes.Length);
			newStream.Flush();
			newStream.Close();


			try
			{

				WebResponse response = request.GetResponse();
				Console.WriteLine("tryyyyyyyyyyyyy");
				Console.WriteLine(((HttpWebResponse)response).StatusDescription);
				Console.WriteLine("in try");

			}
			catch (WebException webex)
			{
				WebResponse errResp = webex.Response;
				using (Stream respStream = errResp.GetResponseStream())
				{
					Console.WriteLine("in catch");
					StreamReader reader = new StreamReader(respStream);
					string text = reader.ReadToEnd();
					Console.WriteLine(text);
				}
			}

			var res = request.GetResponse();

			var stream = res.GetResponseStream();
			var sr = new StreamReader(stream);
			var content = sr.ReadToEnd();


			// Set the content length of the string being posted.
			/*request.ContentLength = byte1.Length;

			Stream writer = request.GetRequestStream();

			writer.Write(byte1, 0, byte1.Length);

			Console.WriteLine("The value of 'ContentLength' property after sending the data is {0}", request.ContentLength);
			writer.Close();*/

			/*using (var client = new WebClient())
			{
				string result = client.DownloadString("http://192.168.99.100:8080/api/message");
				Console.WriteLine("--------------------------------here------------------------------");
				// now use a JSON parser to parse the resulting string back to some CLR object
				Console.WriteLine(result);
			}*/





			//StreamReader sr = new StreamReader(request.GetResponse().GetResponseStream());
			//string Result = sr.ReadToEnd();
			//Console.WriteLine(Result);
			/*WebResponse response = request.GetResponse();
			StreamReader reader = new System.IO.StreamReader(response.GetResponseStream());
			var result = reader.ReadToEnd();
			Console.Write(result);*/

			// Create POST data and convert it to a byte array.  

		}

		/*void OnChange(NetworkReachabilityFlags flags)
		{
			Console.WriteLine("New state for host: " + flags);
		}*/

		



		public override void DidReceiveMemoryWarning()
		{
			base.DidReceiveMemoryWarning();
			// Release any cached data, images, etc that aren't in use.
		}
	}
}
