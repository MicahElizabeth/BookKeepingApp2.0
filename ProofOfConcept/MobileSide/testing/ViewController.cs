using System;
using UIKit;
using Npgsql;

namespace testing
{
	public partial class ViewController : UIViewController
	{
		static string path = "Host=localhost; Username=postgres; Password=whoknows0; Database=test";
		NpgsqlConnection conn = new NpgsqlConnection(path);


		partial void SendButton_TouchUpInside(UIButton sender)
		{
			if (mtext.Text != null)
			{
				string txt = mtext.Text;

				conn.Open();
				//string command = "SELECT distinct sid FROM mtest ORDER BY sid";
				string command = "INSERT INTO mtest(sid, message, reply)" +
					"VALUES ('000','" + txt + "','rep0');";
				// Define a query
				NpgsqlCommand cmd = new NpgsqlCommand(command, conn);

				// Execute a query
				NpgsqlDataReader dr = cmd.ExecuteReader();
			}
		}


		protected ViewController(IntPtr handle) : base(handle)
		{
			// Note: this .ctor should not contain any initialization logic.
		}

		public override void ViewDidLoad()
		{
			base.ViewDidLoad();

			sendButton.SetTitle("Send message", UIControlState.Normal);

			/*
			string path = "Host=localhost; Username=postgres; Password=whoknows0; Database=test";

			// Perform any additional setup after loading the view, typically from a nib.

			// Specify connection options and open an connection
			NpgsqlConnection conn = new NpgsqlConnection(path);

			conn.Open();
			string command = "SELECT distinct sid FROM mtest ORDER BY sid";
			//string command = "INSERT INTO mtest(sid, message, reply)" +
			//	"VALUES ('000', 'hello0', 'rep0');";
			// Define a query
			NpgsqlCommand cmd = new NpgsqlCommand(command, conn);


			// Execute a query
			NpgsqlDataReader dr = cmd.ExecuteReader();

			// Read all rows and output the first column in each row
			while (dr.Read())
				Console.WriteLine(dr.GetString(0));

			// Close connection
			conn.Close();*/

			/*
			string[] states = new string[] { "CA", "ID", "OR", "WA" };

			UITableView _table;

			_table = new UITableView
			{
				Frame = new CoreGraphics.CGRect(0, 30, View.Bounds.Width, View.Bounds.Height),
				Source = new tableSource(states)
			};

			View.AddSubview(_table);*/



		}

		public override void DidReceiveMemoryWarning()
		{
			base.DidReceiveMemoryWarning();
			// Release any cached data, images, etc that aren't in use.
		}
	}
}
