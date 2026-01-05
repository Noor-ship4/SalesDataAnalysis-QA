Start
Set threshold = 100

Input salesData
Input inventoryData

If (salesData is invalid OR inventoryData is invalid) then
    Print "Error: Invalid sales or inventory data"
    End
End If

For each product in salesData do
    If (salesQuantity > threshold) then
    Mark product as "Best Seller"
Else If (salesQuantity >= 50) then
    Mark product as "Average Seller"
Else
    Mark product as "Low Seller"
End If

    Update sales and inventory records
End For

Generate sales analysis report
End
