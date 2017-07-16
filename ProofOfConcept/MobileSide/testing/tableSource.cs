using System;
using UIKit;

namespace testing
{
	public class tableSource : UITableViewSource
	{
		String[] _items;
		String _cellIdentifier = "TableCell";


		public tableSource(String[] items)
		{
			_items = items;
		}


		public override nint RowsInSection(UITableView tableview, nint section)
		{
			return _items.Length;
		}

		public override UITableViewCell GetCell(UITableView tableView, Foundation.NSIndexPath indexPath)
		{
			UITableViewCell cell = tableView.DequeueReusableCell(_cellIdentifier);
			if (cell == null)
			{
				cell = new UITableViewCell(UITableViewCellStyle.Default, _cellIdentifier);
			}
			cell.TextLabel.Text = _items[indexPath.Row];
			return cell;
		}
	}
}
