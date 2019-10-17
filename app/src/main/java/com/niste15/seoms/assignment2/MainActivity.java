package com.niste15.seoms.assignment2;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;

import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.maps.android.data.kml.KmlLayer;

import org.xmlpull.v1.XmlPullParserException;

import java.io.IOException;

public class MainActivity extends AppCompatActivity implements OnMapReadyCallback {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        // Retrieve the content view that renders the map.
        setContentView(R.layout.activity_main);
        // Get the SupportMapFragment and request notification
        // when the map is ready to be used.
        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
                .findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);
    }

    @Override
    public void onMapReady(final GoogleMap googleMap) {
        final KmlLayer[] layer = {null};

        findViewById(R.id.normal).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                try {
                    if (layer[0] != null) {
                        layer[0].removeLayerFromMap();
                    }
                    layer[0] = new KmlLayer(googleMap, R.raw.driving, getApplicationContext());
                    layer[0].addLayerToMap();
                } catch (XmlPullParserException | IOException e) {
                    e.printStackTrace();
                }
            }
        });
        findViewById(R.id.median).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                try {
                    if (layer[0] != null) {
                        layer[0].removeLayerFromMap();
                    }
                    layer[0] = new KmlLayer(googleMap, R.raw.driving_median, getApplicationContext());
                    layer[0].addLayerToMap();
                } catch (XmlPullParserException | IOException e) {
                    e.printStackTrace();
                }
            }
        });
        findViewById(R.id.mean).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                try {
                    if (layer[0] != null) {
                        layer[0].removeLayerFromMap();
                    }
                    layer[0] = new KmlLayer(googleMap, R.raw.driving_mean, getApplicationContext());
                    layer[0].addLayerToMap();
                } catch (XmlPullParserException | IOException e) {
                    e.printStackTrace();
                }
            }
        });



        //try {
        //    layer[0] = new KmlLayer(googleMap, R.raw.driving, getApplicationContext());
        //    layer[0].addLayerToMap();
        //} catch (XmlPullParserException | IOException e) {
        //    e.printStackTrace();
        //}
    }
}