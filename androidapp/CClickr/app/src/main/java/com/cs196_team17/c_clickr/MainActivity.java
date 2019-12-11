package com.cs196_team17.c_clickr;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;

import android.content.Context;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

public class MainActivity extends AppCompatActivity {

    public static int[] COLOR_IDS = new int[] {R.drawable.red_box, R.drawable.green_box, R.drawable.blue_box, R.drawable.yellow_box};
    private String uid, uin;

    private TextView textViewUIN;

    private View[][] boxes = new View[4][4];

    private DatabaseReference database;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        setGrid("0000111122223333");

        textViewUIN = findViewById(R.id.label_uin);

        uid = getIntent().getStringExtra("UID");

        database = FirebaseDatabase.getInstance().getReference();

        if (getIntent().hasExtra("UIN")) {
            database.child("users").child(uid).child("UIN").setValue(getIntent().getStringExtra("UIN"));
        }

        ValueEventListener uinListener = new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                try {
                    uin = dataSnapshot.getValue().toString();
                    Log.d("firebase", "UIN: " + uin);
                    textViewUIN.setText("UIN: " + uin);
                    String uinBase4 = Long.toString(Long.parseLong(uin, 10), 4);
                    uinBase4 = String.format("%1$" + 16 + "s", uinBase4).replace(' ', '0');
                    Log.d("UINBASE", uinBase4);
                    setGrid(uinBase4);
                } catch (NullPointerException e) {
                    e.printStackTrace();
                }
            }

            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {

            }
        };

        database.child("users").child(uid).child("UIN").addValueEventListener(uinListener);
    }

    private void setGrid(String base4code) {
        int[][] nums = new int[4][4];

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                nums[i][j] = Integer.parseInt(base4code.substring(i*4+j, i*4+j+1));
            }
        }

        for (int r = 0; r < boxes.length; r++) {
            for (int c = 0; c < boxes[r].length; c++) {
                Context context = getApplicationContext();
                String boxID = "box_" + r + "_" + c;
                int id = getApplicationContext().getResources().getIdentifier(boxID, "id", context.getPackageName());
                boxes[r][c] = findViewById(id);
                boxes[r][c].setBackground(ContextCompat.getDrawable(getApplicationContext(), COLOR_IDS[nums[r][c]]));
            }
        }
    }
}
