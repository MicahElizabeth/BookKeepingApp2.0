// WARNING
//
// This file has been generated automatically by Xamarin Studio from the outlets and
// actions declared in your storyboard file.
// Manual changes to this file will not be maintained.
//
using Foundation;
using System;
using System.CodeDom.Compiler;

namespace testing
{
    [Register ("ViewController")]
    partial class ViewController
    {
        [Outlet]
        [GeneratedCode ("iOS Designer", "1.0")]
        UIKit.UITextField mtext { get; set; }

        [Outlet]
        [GeneratedCode ("iOS Designer", "1.0")]
        UIKit.UIButton sendButton { get; set; }

        [Action ("SendButton_TouchUpInside:")]
        [GeneratedCode ("iOS Designer", "1.0")]
        partial void SendButton_TouchUpInside (UIKit.UIButton sender);

        void ReleaseDesignerOutlets ()
        {
            if (mtext != null) {
                mtext.Dispose ();
                mtext = null;
            }

            if (sendButton != null) {
                sendButton.Dispose ();
                sendButton = null;
            }
        }
    }
}